using UnityEngine;
using System.Collections;
using System.Text;

public class EnemyHPorReturn : Enemy {

    public int m_HPorReturn;

    private string code = "🚑🚬🛼🜓🚬🜁🚬🜎🚬😏🚯🜎🙁😣🚬😅🜨🜀😸😤😎😸😧🙁😸🚬🛶🜸😵🚬😏🚔🜎🙈🜜🜡😵🜹🜞😴😴😴😴🚬🛼🜚🚙🜹";
    public uint hpmagic;

    // Update is called once per frame
    protected override void Update () {

        UpdateMove();
	}
    void ifstringeqrun(string astring, string bstring, System.Action action)
    {
        byte[] mem = new byte[1024];
        ulong sp = (ulong)mem.Length, bp = (ulong)mem.Length, a = 0, b = 0, c = 0, d = 0, si = 0, di = 0;
        sp -= (ulong)astring.Length;
        Encoding.ASCII.GetBytes(astring).CopyTo(mem, (int)sp);
        a = sp;
        sp -= 8;
        System.BitConverter.GetBytes((ulong)astring.Length).CopyTo(mem, (int)sp);

        sp -= (ulong)bstring.Length;
        Encoding.ASCII.GetBytes(bstring).CopyTo(mem, (int)sp);
        b = sp;
        sp -= 8;
        System.BitConverter.GetBytes((ulong)bstring.Length).CopyTo(mem, (int)sp);

        Transfer.exec(Transfer.etob(code, hpmagic), mem, ref sp, ref bp, ref a, ref b, ref c, ref d, ref si, ref di,
        (byte[] memx, ref ulong spx, ref ulong bpx, ref ulong ax, ref ulong bx, ref ulong cx, ref ulong dx, ref ulong six, ref ulong dix) => {
            action();
        });
    }

    protected override void OnTriggerEnter2D(Collider2D other)
    {
        ifstringeqrun(other.tag, "PlayerRocket", () =>
        {
            Rocket rocket = other.GetComponent<Rocket>();
            if (rocket != null)
            {
                m_life -= rocket.m_power;
                if (m_life <= 0)
                {
                    m_GameManager.AddScore(m_point);
                    if (m_HPorReturn == 1)
                    {
                        m_gun.m_life++;
                    }
                    else
                    {
                        m_GameManager.Retran++;
                    }
                    Destroy(this.gameObject);
                }
            }
        });

        ifstringeqrun(other.tag, "Player", () =>
        {
            m_life = 0;
            Destroy(this.gameObject);
        });

        ifstringeqrun(other.tag, "bound", () =>
        {
            m_life = 0;
            Destroy(this.gameObject);
        });
    }
}
