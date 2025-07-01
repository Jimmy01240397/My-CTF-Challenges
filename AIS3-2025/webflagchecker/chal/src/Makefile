dir := bin
js := index.js
frontend := index.html
src := main.c

all: $(dir) $(dir)/$(js) $(addprefix $(dir)/,$(frontend))

$(dir):
	mkdir -p $(dir)

$(dir)/$(js): $(src)
	emcc $< -sEXPORTED_FUNCTIONS='["_flagchecker","_on_check","_main"]' -sWASM=1 -o $@ -sALLOW_MEMORY_GROWTH -sEXPORTED_RUNTIME_METHODS=stringToUTF8,lengthBytesUTF8

$(dir)/%: %
	cp $< $@

clean:
	rm -rf $(dir)




