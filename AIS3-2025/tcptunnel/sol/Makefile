dir := bin
exe := exploitbydev
src := exploitbydev.c

all: $(dir)/$(exe)

$(dir)/$(exe): $(src)
	mkdir -p $(dir)
	gcc $< -o $@

clean:
	rm -rf $(dir)




