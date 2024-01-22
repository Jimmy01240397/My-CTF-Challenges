py := python3
builder := nasm
linker := ld
builddir := bin
obj := obj

all: $(builddir)/flagcode.txt $(builddir)/strcmp-gun.txt $(builddir)/strcmp-boss.txt $(builddir)/strcmp-enemy.txt $(builddir)/strcmp-hp.txt

$(builddir)/flagcode.txt: $(obj)/flagcode_textonly bytetoemoji.py $(builddir)
	$(py) bytetoemoji.py $< 228 > $@

$(obj)/flagcode_textonly: $(obj)/flagcode
	dd if=$< of=$@ bs=1055 count=1 skip=4096 iflag=skip_bytes

$(obj)/flagcode: $(obj)/flagcode.o
	$(linker) -o $@ $<

$(obj)/flagcode.o: $(obj)/flagcode.s
	$(builder) -f elf64 -o $@ $<

$(obj)/flagcode.s: flagcodegenerater.py $(obj)
	$(py) $< > $@

$(builddir)/strcmp-gun.txt: $(obj)/strcmp_textonly bytetoemoji.py $(builddir)
	$(py) bytetoemoji.py $< 117 > $@

$(builddir)/strcmp-boss.txt: $(obj)/strcmp_textonly bytetoemoji.py $(builddir)
	$(py) bytetoemoji.py $< 64 > $@

$(builddir)/strcmp-enemy.txt: $(obj)/strcmp_textonly bytetoemoji.py $(builddir)
	$(py) bytetoemoji.py $< 87 > $@

$(builddir)/strcmp-hp.txt: $(obj)/strcmp_textonly bytetoemoji.py $(builddir)
	$(py) bytetoemoji.py $< 52 > $@

$(obj)/strcmp_textonly: $(obj)/strcmp
	dd if=$< of=$@ bs=48 count=1 skip=4096 iflag=skip_bytes

$(obj)/strcmp: $(obj)/strcmp.o
	$(linker) -o $@ $<

$(obj)/strcmp.o: strcmp.s
	$(builder) -f elf64 -o $@ $<

$(builddir):
	mkdir $@

$(obj):
	mkdir $@

clean: 
	rm -rf $(builddir)
	rm -rf $(obj)
