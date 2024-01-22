using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Runtime.InteropServices;
using System.Text;

public static unsafe class Transfer
{
    public delegate void Callfunc(byte[] mem, ref ulong sp, ref ulong bp, ref ulong a, ref ulong b, ref ulong c, ref ulong d, ref ulong si, ref ulong di);
    delegate void modrmfunc<T>(byte regcode, T* reg, T* mem) where T : unmanaged;
    public static void exec(byte[] code, byte[] mem, ref ulong sp, ref ulong bp, ref ulong a, ref ulong b, ref ulong c, ref ulong d, ref ulong si, ref ulong di, params Callfunc[] callfuncs)
    {
        fixed (ulong* spptr = &sp,
                     bpptr = &bp,
                     aptr = &a,
                     bptr = &b,
                     cptr = &c,
                     dptr = &d,
                     siptr = &si,
                     diptr = &di)
        {
            ulong*[] regptr = new ulong*[] { aptr, cptr, dptr, bptr, spptr, bpptr, siptr, diptr };
            byte bytelong = 4;
            int cmpresult = 0;

            void modrm<T>(ref int pc, modrmfunc<T> action, bool bytemode = false) where T : unmanaged
            {
                bool regH = false;
                if (bytemode && ((code[pc] >> 5) & 0b00000001) == 0x1) regH = true;
                byte regmask = 0b00000111;
                if (bytemode) regmask = 0b00000011;
                T* reg = null, memreg = null;
                byte regcode = (byte)((code[pc] >> 3) & 0b00000111);
                switch (code[pc] >> 6)
                {
                    case 0b00:
                        {
                            switch ((code[pc]) & 0b00000111)
                            {
                                case 0b100:
                                    {
                                        int left = (code[pc + 1] >> 6) & 0b00000011;
                                        ulong index = 0;
                                        if (((code[pc + 1] >> 3) & 0b00000111) != 0b100)
                                            index = ((*regptr[(code[pc + 1] >> 3) & 0b00000111]) << left);

                                        reg = (T*)regptr[(code[pc] >> 3) & regmask];
                                        if (regH)
                                        {
                                            reg = (T*)(((byte*)reg) + 1);
                                        }
                                        fixed (byte* tmp = &mem[*regptr[(code[pc + 1]) & 0b00000111] + index])
                                        {
                                            memreg = (T*)tmp;
                                        }

                                        pc++;
                                    }
                                    break;
                                case 0b101:
                                    {

                                    }
                                    break;
                                default:
                                    {
                                        reg = (T*)regptr[(code[pc] >> 3) & regmask];
                                        if (regH)
                                        {
                                            reg = (T*)(((byte*)reg) + 1);
                                        }
                                        fixed (byte* tmp = &mem[(long)*regptr[(code[pc]) & 0b00000111]])
                                        {
                                            memreg = (T*)tmp;
                                        }
                                    }
                                    break;
                            }
                        }
                        break;
                    case 0b01:
                        {
                            sbyte offset = (sbyte)code[pc + 1];
                            reg = (T*)regptr[(code[pc] >> 3) & regmask];
                            if (regH)
                            {
                                reg = (T*)(((byte*)reg) + 1);
                            }
                            fixed (byte* tmp = &mem[(long)*regptr[(code[pc]) & 0b00000111] + offset])
                            {
                                memreg = (T*)tmp;
                            }
                            pc++;
                        }
                        break;
                    case 0b10:
                        {
                            int offset = BitConverter.ToInt32(code, pc + 1);
                            reg = (T*)regptr[(code[pc] >> 3) & regmask];
                            if (regH)
                            {
                                reg = (T*)(((byte*)reg) + 1);
                            }
                            fixed (byte* tmp = &mem[(long)*regptr[(code[pc]) & 0b00000111] + offset])
                            {
                                memreg = (T*)tmp;
                            }
                            pc += 4;
                        }
                        break;
                    case 0b11:
                        {
                            reg = (T*)regptr[(code[pc] >> 3) & regmask];
                            memreg = (T*)regptr[(code[pc]) & regmask];
                            if (regH)
                            {
                                reg = (T*)(((byte*)reg) + 1);
                                memreg = (T*)(((byte*)memreg) + 1);
                            }
                        }
                        break;
                }
                action(regcode, reg, memreg);
            }


            for (int pc = 0; pc < code.Length; pc++)
            {
                switch (code[pc])
                {
                    #region push
                    case 0x50:
                    case 0x51:
                    case 0x52:
                    case 0x53:
                    case 0x54:
                    case 0x55:
                    case 0x56:
                    case 0x57:
                        {
                            ulong tmp = *regptr[code[pc] - 0x50];
                            sp -= 8;
                            BitConverter.GetBytes(tmp).CopyTo(mem, (int)sp);
                        }
                        break;
                    #endregion
                    #region pop
                    case 0x58:
                    case 0x59:
                    case 0x5A:
                    case 0x5B:
                    case 0x5C:
                    case 0x5D:
                    case 0x5E:
                    case 0x5F:
                        {
                            ulong tmp = BitConverter.ToUInt64(mem, (int)sp);
                            sp += 8;
                            *regptr[code[pc] - 0x58] = tmp;
                        }
                        break;
                    #endregion
                    #region mov
                    case 0x88:
                        {
                            pc++;
                            modrm<byte>(ref pc, (regcode, src, dst) =>
                            {
                                *dst = *src;
                            }, true);
                        }
                        break;
                    case 0x89:
                        {
                            pc++;
                            switch (bytelong)
                            {
                                case 2:
                                    modrm<ushort>(ref pc, (regcode, src, dst) =>
                                    {
                                        *dst = *src;
                                    });
                                    break;
                                case 4:
                                    modrm<uint>(ref pc, (regcode, src, dst) =>
                                    {
                                        *dst = *src;
                                    });
                                    break;
                                case 8:
                                    modrm<ulong>(ref pc, (regcode, src, dst) =>
                                    {
                                        *dst = *src;
                                    });
                                    break;
                            }
                        }
                        break;
                    case 0x8A:
                        {
                            pc++;
                            modrm<byte>(ref pc, (regcode, dst, src) =>
                            {
                                *dst = *src;
                            }, true);
                        }
                        break;
                    case 0x8B:
                        {
                            pc++;
                            switch (bytelong)
                            {
                                case 2:
                                    modrm<ushort>(ref pc, (regcode, dst, src) =>
                                    {
                                        *dst = *src;
                                    });
                                    break;
                                case 4:
                                    modrm<uint>(ref pc, (regcode, dst, src) =>
                                    {
                                        *dst = *src;
                                    });
                                    break;
                                case 8:
                                    modrm<ulong>(ref pc, (regcode, dst, src) =>
                                    {
                                        *dst = *src;
                                    });
                                    break;
                            }
                        }
                        break;
                    case 0xB0:
                    case 0xB1:
                    case 0xB2:
                    case 0xB3:
                        {
                            byte data = code[pc + 1];
                            *(byte*)regptr[code[pc] - 0xB0] = data;
                            pc++;
                        }
                        break;
                    case 0xB4:
                    case 0xB5:
                    case 0xB6:
                    case 0xB7:
                        {
                            byte data = code[pc + 1];
                            *((byte*)regptr[code[pc] - 0xB0] + 1) = data;
                            pc++;
                        }
                        break;
                    case 0xB8:
                    case 0xB9:
                    case 0xBA:
                    case 0xBB:
                    case 0xBC:
                    case 0xBD:
                    case 0xBE:
                    case 0xBF:
                        {
                            switch (bytelong)
                            {
                                case 2:
                                    {
                                        ushort data = BitConverter.ToUInt16(code, pc + 1);
                                        *(ushort*)regptr[code[pc] - 0xB8] = data;
                                    }
                                    break;
                                case 4:
                                    {
                                        uint data = BitConverter.ToUInt32(code, pc + 1);
                                        *(uint*)regptr[code[pc] - 0xB8] = data;
                                    }
                                    break;
                                case 8:
                                    {
                                        ulong data = BitConverter.ToUInt64(code, pc + 1);
                                        *regptr[code[pc] - 0xB8] = data;
                                    }
                                    break;
                            }

                            pc += bytelong;
                        }
                        break;
                    #endregion
                    #region op
                    case 0x80:
                        {
                            pc++;
                            modrm<byte>(ref pc, (modecode, nop, dst) =>
                            {
                                pc++;
                                byte data = code[pc];
                                switch (modecode)
                                {
                                    case 0:
                                        *dst += data;
                                        break;
                                    case 1:
                                        *dst |= data;
                                        break;
                                    case 2:
                                            //adc
                                            break;
                                    case 3:
                                            //sbb
                                            break;
                                    case 4:
                                        *dst &= data;
                                        break;
                                    case 5:
                                        *dst -= data;
                                        break;
                                    case 6:
                                        *dst ^= data;
                                        break;
                                    case 7:
                                        cmpresult = (*dst).CompareTo(data);
                                        break;
                                }
                            }, true);
                        }
                        break;
                    case 0x83:
                        {
                            pc++;
                            switch (bytelong)
                            {
                                case 2:
                                    modrm<ushort>(ref pc, (modecode, nop, dst) =>
                                    {
                                        pc++;
                                        byte data = code[pc];
                                        switch (modecode)
                                        {
                                            case 0:
                                                *dst += data;
                                                break;
                                            case 1:
                                                *dst |= data;
                                                break;
                                            case 2:
                                                    //adc
                                                    break;
                                            case 3:
                                                    //sbb
                                                    break;
                                            case 4:
                                                *dst &= data;
                                                break;
                                            case 5:
                                                *dst -= data;
                                                break;
                                            case 6:
                                                *dst ^= data;
                                                break;
                                            case 7:
                                                cmpresult = (*dst).CompareTo(data);
                                                break;
                                        }
                                    });
                                    break;
                                case 4:
                                    modrm<uint>(ref pc, (modecode, nop, dst) =>
                                    {
                                        pc++;
                                        byte data = code[pc];
                                        switch (modecode)
                                        {
                                            case 0:
                                                *dst += data;
                                                break;
                                            case 1:
                                                *dst |= data;
                                                break;
                                            case 2:
                                                    //adc
                                                    break;
                                            case 3:
                                                    //sbb
                                                    break;
                                            case 4:
                                                *dst &= data;
                                                break;
                                            case 5:
                                                *dst -= data;
                                                break;
                                            case 6:
                                                *dst ^= data;
                                                break;
                                            case 7:
                                                cmpresult = (*dst).CompareTo(data);
                                                break;
                                        }
                                    });
                                    break;
                                case 8:
                                    modrm<uint>(ref pc, (modecode, nop, dst) =>
                                    {
                                        pc++;
                                        byte data = code[pc];
                                        switch (modecode)
                                        {
                                            case 0:
                                                *dst += data;
                                                break;
                                            case 1:
                                                *dst |= data;
                                                break;
                                            case 2:
                                                    //adc
                                                    break;
                                            case 3:
                                                    //sbb
                                                    break;
                                            case 4:
                                                *dst &= data;
                                                break;
                                            case 5:
                                                *dst -= data;
                                                break;
                                            case 6:
                                                *dst ^= data;
                                                break;
                                            case 7:
                                                cmpresult = (*dst).CompareTo(data);
                                                break;
                                        }
                                    });
                                    break;
                            }
                        }
                        break;
                    case 0x81:
                        {
                            pc++;
                            switch (bytelong)
                            {
                                case 2:
                                    modrm<ushort>(ref pc, (modecode, nop, dst) =>
                                    {
                                        ushort data = BitConverter.ToUInt16(code, pc + 1);
                                        switch (modecode)
                                        {
                                            case 0:
                                                *dst += data;
                                                break;
                                            case 1:
                                                *dst |= data;
                                                break;
                                            case 2:
                                                    //adc
                                                    break;
                                            case 3:
                                                    //sbb
                                                    break;
                                            case 4:
                                                *dst &= data;
                                                break;
                                            case 5:
                                                *dst -= data;
                                                break;
                                            case 6:
                                                *dst ^= data;
                                                break;
                                            case 7:
                                                cmpresult = (*dst).CompareTo(data);
                                                break;
                                        }
                                        pc += 2;
                                    });
                                    break;
                                case 4:
                                    modrm<uint>(ref pc, (modecode, nop, dst) =>
                                    {
                                        uint data = BitConverter.ToUInt32(code, pc + 1);
                                        switch (modecode)
                                        {
                                            case 0:
                                                *dst += data;
                                                break;
                                            case 1:
                                                *dst |= data;
                                                break;
                                            case 2:
                                                    //adc
                                                    break;
                                            case 3:
                                                    //sbb
                                                    break;
                                            case 4:
                                                *dst &= data;
                                                break;
                                            case 5:
                                                *dst -= data;
                                                break;
                                            case 6:
                                                *dst ^= data;
                                                break;
                                            case 7:
                                                cmpresult = (*dst).CompareTo(data);
                                                break;
                                        }
                                        pc += 4;
                                    });
                                    break;
                                case 8:
                                    modrm<ulong>(ref pc, (modecode, nop, dst) =>
                                    {
                                        ulong data = (ulong)BitConverter.ToInt32(code, pc + 1);
                                        switch (modecode)
                                        {
                                            case 0:
                                                *dst += data;
                                                break;
                                            case 1:
                                                *dst |= data;
                                                break;
                                            case 2:
                                                    //adc
                                                    break;
                                            case 3:
                                                    //sbb
                                                    break;
                                            case 4:
                                                *dst &= data;
                                                break;
                                            case 5:
                                                *dst -= data;
                                                break;
                                            case 6:
                                                *dst ^= data;
                                                break;
                                            case 7:
                                                cmpresult = (*dst).CompareTo(data);
                                                break;
                                        }
                                        pc += 8;
                                    });
                                    break;
                            }
                        }
                        break;
                    case 0x00:
                    case 0x08:
                    case 0x10:
                    case 0x18:
                    case 0x20:
                    case 0x28:
                    case 0x30:
                    case 0x38:
                        {
                            byte nowcode = code[pc];
                            pc++;
                            modrm<byte>(ref pc, (regcode, src, dst) =>
                            {
                                switch (nowcode)
                                {
                                    case 0x00:
                                        *dst += *src;
                                        break;
                                    case 0x08:
                                        *dst |= *src;
                                        break;
                                    case 0x10:
                                            //adc
                                            break;
                                    case 0x18:
                                            //sbb
                                            break;
                                    case 0x20:
                                        *dst &= *src;
                                        break;
                                    case 0x28:
                                        *dst -= *src;
                                        break;
                                    case 0x30:
                                        *dst ^= *src;
                                        break;
                                    case 0x38:
                                        cmpresult = (*dst).CompareTo(*src);
                                        break;
                                }
                            }, true);
                        }
                        break;
                    case 0x01:
                    case 0x09:
                    case 0x11:
                    case 0x19:
                    case 0x21:
                    case 0x29:
                    case 0x31:
                    case 0x39:
                        {
                            byte nowcode = code[pc];
                            pc++;
                            switch (bytelong)
                            {
                                case 2:
                                    modrm<ushort>(ref pc, (regcode, src, dst) =>
                                    {
                                        switch (nowcode)
                                        {
                                            case 0x01:
                                                *dst += *src;
                                                break;
                                            case 0x09:
                                                *dst |= *src;
                                                break;
                                            case 0x11:
                                                    //adc
                                                    break;
                                            case 0x19:
                                                    //sbb
                                                    break;
                                            case 0x21:
                                                *dst &= *src;
                                                break;
                                            case 0x29:
                                                *dst -= *src;
                                                break;
                                            case 0x31:
                                                *dst ^= *src;
                                                break;
                                            case 0x39:
                                                cmpresult = (*dst).CompareTo(*src);
                                                break;
                                        }
                                    });
                                    break;
                                case 4:
                                    modrm<uint>(ref pc, (regcode, src, dst) =>
                                    {
                                        switch (nowcode)
                                        {
                                            case 0x01:
                                                *dst += *src;
                                                break;
                                            case 0x09:
                                                *dst |= *src;
                                                break;
                                            case 0x11:
                                                    //adc
                                                    break;
                                            case 0x19:
                                                    //sbb
                                                    break;
                                            case 0x21:
                                                *dst &= *src;
                                                break;
                                            case 0x29:
                                                *dst -= *src;
                                                break;
                                            case 0x31:
                                                *dst ^= *src;
                                                break;
                                            case 0x39:
                                                cmpresult = (*dst).CompareTo(*src);
                                                break;
                                        }
                                    });
                                    break;
                                case 8:
                                    modrm<ulong>(ref pc, (regcode, src, dst) =>
                                    {
                                        switch (nowcode)
                                        {
                                            case 0x01:
                                                *dst += *src;
                                                break;
                                            case 0x09:
                                                *dst |= *src;
                                                break;
                                            case 0x11:
                                                    //adc
                                                    break;
                                            case 0x19:
                                                    //sbb
                                                    break;
                                            case 0x21:
                                                *dst &= *src;
                                                break;
                                            case 0x29:
                                                *dst -= *src;
                                                break;
                                            case 0x31:
                                                *dst ^= *src;
                                                break;
                                            case 0x39:
                                                cmpresult = (*dst).CompareTo(*src);
                                                break;
                                        }
                                    });
                                    break;
                            }
                        }
                        break;
                    case 0x02:
                    case 0x0A:
                    case 0x12:
                    case 0x1A:
                    case 0x22:
                    case 0x2A:
                    case 0x32:
                    case 0x3A:
                        {
                            byte nowcode = code[pc];
                            pc++;
                            modrm<byte>(ref pc, (regcode, dst, src) =>
                            {
                                switch (nowcode)
                                {
                                    case 0x02:
                                        *dst += *src;
                                        break;
                                    case 0x0A:
                                        *dst |= *src;
                                        break;
                                    case 0x12:
                                            //adc
                                            break;
                                    case 0x1A:
                                            //sbb
                                            break;
                                    case 0x22:
                                        *dst &= *src;
                                        break;
                                    case 0x2A:
                                        *dst -= *src;
                                        break;
                                    case 0x32:
                                        *dst ^= *src;
                                        break;
                                    case 0x3A:
                                        cmpresult = (*dst).CompareTo(*src);
                                        break;
                                }
                            }, true);
                        }
                        break;
                    case 0x03:
                    case 0x0B:
                    case 0x13:
                    case 0x1B:
                    case 0x23:
                    case 0x2B:
                    case 0x33:
                    case 0x3B:
                        {
                            byte nowcode = code[pc];
                            pc++;
                            switch (bytelong)
                            {
                                case 2:
                                    modrm<ushort>(ref pc, (regcode, dst, src) =>
                                    {
                                        switch (nowcode)
                                        {
                                            case 0x03:
                                                *dst += *src;
                                                break;
                                            case 0x0B:
                                                *dst |= *src;
                                                break;
                                            case 0x13:
                                                    //adc
                                                    break;
                                            case 0x1B:
                                                    //sbb
                                                    break;
                                            case 0x23:
                                                *dst &= *src;
                                                break;
                                            case 0x2B:
                                                *dst -= *src;
                                                break;
                                            case 0x33:
                                                *dst ^= *src;
                                                break;
                                            case 0x3B:
                                                cmpresult = (*dst).CompareTo(*src);
                                                break;
                                        }
                                    });
                                    break;
                                case 4:
                                    modrm<uint>(ref pc, (regcode, dst, src) =>
                                    {
                                        switch (nowcode)
                                        {
                                            case 0x03:
                                                *dst += *src;
                                                break;
                                            case 0x0B:
                                                *dst |= *src;
                                                break;
                                            case 0x13:
                                                    //adc
                                                    break;
                                            case 0x1B:
                                                    //sbb
                                                    break;
                                            case 0x23:
                                                *dst &= *src;
                                                break;
                                            case 0x2B:
                                                *dst -= *src;
                                                break;
                                            case 0x33:
                                                *dst ^= *src;
                                                break;
                                            case 0x3B:
                                                cmpresult = (*dst).CompareTo(*src);
                                                break;
                                        }
                                    });
                                    break;
                                case 8:
                                    modrm<ulong>(ref pc, (regcode, dst, src) =>
                                    {
                                        switch (nowcode)
                                        {
                                            case 0x03:
                                                *dst += *src;
                                                break;
                                            case 0x0B:
                                                *dst |= *src;
                                                break;
                                            case 0x13:
                                                    //adc
                                                    break;
                                            case 0x1B:
                                                    //sbb
                                                    break;
                                            case 0x23:
                                                *dst &= *src;
                                                break;
                                            case 0x2B:
                                                *dst -= *src;
                                                break;
                                            case 0x33:
                                                *dst ^= *src;
                                                break;
                                            case 0x3B:
                                                cmpresult = (*dst).CompareTo(*src);
                                                break;
                                        }
                                    });
                                    break;
                            }
                        }
                        break;
                    case 0x04:
                    case 0x0C:
                    case 0x14:
                    case 0x1C:
                    case 0x24:
                    case 0x2C:
                    case 0x34:
                    case 0x3C:
                        {
                            byte nowcode = code[pc];
                            byte data = code[pc + 1];
                            switch (nowcode)
                            {
                                case 0x04:
                                    *(byte*)regptr[0] += data;
                                    break;
                                case 0x0C:
                                    *(byte*)regptr[0] |= data;
                                    break;
                                case 0x14:
                                    //adc
                                    break;
                                case 0x1C:
                                    //sbb
                                    break;
                                case 0x24:
                                    *(byte*)regptr[0] &= data;
                                    break;
                                case 0x2C:
                                    *(byte*)regptr[0] -= data;
                                    break;
                                case 0x34:
                                    *(byte*)regptr[0] ^= data;
                                    break;
                                case 0x3C:
                                    cmpresult = (*(byte*)regptr[0]).CompareTo(data);
                                    break;
                            }
                            pc++;
                        }
                        break;

                    case 0x05:
                    case 0x0D:
                    case 0x15:
                    case 0x1D:
                    case 0x25:
                    case 0x2D:
                    case 0x35:
                    case 0x3D:
                        {
                            byte nowcode = code[pc];
                            switch (bytelong)
                            {
                                case 2:
                                    {
                                        ushort data = BitConverter.ToUInt16(code, pc + 1);
                                        switch (nowcode)
                                        {
                                            case 0x05:
                                                *(ushort*)regptr[0] += data;
                                                break;
                                            case 0x0D:
                                                *(ushort*)regptr[0] |= data;
                                                break;
                                            case 0x15:
                                                //adc
                                                break;
                                            case 0x1D:
                                                //sbb
                                                break;
                                            case 0x25:
                                                *(ushort*)regptr[0] &= data;
                                                break;
                                            case 0x2D:
                                                *(ushort*)regptr[0] -= data;
                                                break;
                                            case 0x35:
                                                *(ushort*)regptr[0] ^= data;
                                                break;
                                            case 0x3D:
                                                cmpresult = (*(ushort*)regptr[0]).CompareTo(data);
                                                break;
                                        }
                                        pc += 2;
                                    }
                                    break;
                                case 4:
                                    {
                                        uint data = BitConverter.ToUInt32(code, pc + 1);
                                        switch (nowcode)
                                        {
                                            case 0x05:
                                                *(uint*)regptr[0] += data;
                                                break;
                                            case 0x0D:
                                                *(uint*)regptr[0] |= data;
                                                break;
                                            case 0x15:
                                                //adc
                                                break;
                                            case 0x1D:
                                                //sbb
                                                break;
                                            case 0x25:
                                                *(uint*)regptr[0] &= data;
                                                break;
                                            case 0x2D:
                                                *(uint*)regptr[0] -= data;
                                                break;
                                            case 0x35:
                                                *(uint*)regptr[0] ^= data;
                                                break;
                                            case 0x3D:
                                                cmpresult = (*(uint*)regptr[0]).CompareTo(data);
                                                break;
                                        }
                                        pc += 4;
                                    }
                                    break;
                                case 8:
                                    {
                                        ulong data = (ulong)BitConverter.ToInt32(code, pc + 1);
                                        switch (nowcode)
                                        {
                                            case 0x05:
                                                *regptr[0] += data;
                                                break;
                                            case 0x0D:
                                                *regptr[0] |= data;
                                                break;
                                            case 0x15:
                                                //adc
                                                break;
                                            case 0x1D:
                                                //sbb
                                                break;
                                            case 0x25:
                                                *regptr[0] &= data;
                                                break;
                                            case 0x2D:
                                                *regptr[0] -= data;
                                                break;
                                            case 0x35:
                                                *regptr[0] ^= data;
                                                break;
                                            case 0x3D:
                                                cmpresult = (*regptr[0]).CompareTo(data);
                                                break;
                                        }
                                        pc += 4;
                                    }
                                    break;
                            }
                        }
                        break;

                    #endregion
                    #region jmp
                    case 0xEB:
                        {
                            sbyte offset = (sbyte)code[pc + 1];
                            pc++;
                            pc += offset;
                        }
                        break;
                    case 0xE9:
                        {
                            int offset = BitConverter.ToInt32(code, pc + 1);
                            pc += 4;
                            pc += offset;
                        }
                        break;
                    case 0x74:
                    case 0x75:
                    case 0x7C:
                    case 0x7D:
                    case 0x7E:
                    case 0x7F:
                        {
                            byte jmpcode = code[pc];
                            sbyte offset = (sbyte)code[pc + 1];
                            pc++;
                            switch (jmpcode)
                            {
                                case 0x74:
                                    if (cmpresult == 0) pc += offset;
                                    break;
                                case 0x75:
                                    if (cmpresult != 0) pc += offset;
                                    break;
                                case 0x7C:
                                    if (cmpresult < 0) pc += offset;
                                    break;
                                case 0x7D:
                                    if (cmpresult >= 0) pc += offset;
                                    break;
                                case 0x7E:
                                    if (cmpresult <= 0) pc += offset;
                                    break;
                                case 0x7F:
                                    if (cmpresult > 0) pc += offset;
                                    break;
                            }
                        }
                        break;
                    case 0x0F:
                        {
                            pc++;
                            byte jmpcode = code[pc];
                            int offset = BitConverter.ToInt32(code, pc + 1);
                            pc += 4;
                            switch (jmpcode)
                            {
                                case 0x84:
                                    if (cmpresult == 0) pc += offset;
                                    break;
                                case 0x85:
                                    if (cmpresult != 0) pc += offset;
                                    break;
                                case 0x8C:
                                    if (cmpresult < 0) pc += offset;
                                    break;
                                case 0x8D:
                                    if (cmpresult >= 0) pc += offset;
                                    break;
                                case 0x8E:
                                    if (cmpresult <= 0) pc += offset;
                                    break;
                                case 0x8F:
                                    if (cmpresult > 0) pc += offset;
                                    break;
                            }
                        }
                        break;
                    #endregion
                    case 0xE8:
                        {
                            int index = BitConverter.ToInt32(code, pc + 1);
                            callfuncs[index](mem, ref sp, ref bp, ref a, ref b, ref c, ref d, ref si, ref di);
                        }
                        break;
                    case 0xC3:
                        return;
                    case 0x66:
                        bytelong = 2;
                        continue;
                    default:
                        {
                            bool isprefix = (code[pc] & 0b11110000) == 0b01000000;
                            if (isprefix)
                            {
                                bytelong = (code[pc] & 0b00001000) == 0b00001000 ? (byte)8 : bytelong;
                                continue;
                            }
                            else
                            {
                            }
                        }
                        break;
                }
                bytelong = 4;
            }
        }
    }

    public static byte[] etob(string data, uint magic)
    {
        byte[] databyte = Encoding.UTF32.GetBytes(data);
        using (MemoryStream stream = new MemoryStream())
        {
            for (int i = 0; i < databyte.Length; i += 4)
            {
                uint now = BitConverter.ToUInt32(databyte, i);
                if (now >= 0x1f700)
                    now -= 3;
                if (now >= 0x1f6f0)
                    now -= 3;
                if (now >= 0x1f6dd)
                    now -= 5;
                if (now >= 0x1f6d5)
                    now -= 2;
                if (now >= 0x1f6cb)
                    now -= 5;
                if (now >= 0x1f680)
                    now -= 48;
                now ^= magic;
                if (now < 0x0001F600 || now > 0x0001F6FF) continue;
                now -= 0x0001F600;
                stream.WriteByte((byte)now);
            }
            return stream.ToArray();
        }
    }

    static public string BytesToHex(byte[] bytes)
    {
        StringBuilder str2 = new StringBuilder();
        for (int i = 0; i < bytes.Length; i++)
        {
            str2.Append(bytes[i].ToString("X2"));
        }
        return str2.ToString();
    }
}
