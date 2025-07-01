dir := bin
exe := tcptunnel
src := main.c

all: $(dir)/$(exe)

$(dir)/$(exe): $(src)
	mkdir -p $(dir)
	gcc $< -o $@

clean:
	rm -rf $(dir)




