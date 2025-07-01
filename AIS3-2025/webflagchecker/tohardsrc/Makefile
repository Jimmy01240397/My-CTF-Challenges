dir := bin
wasm := web/app.wasm
frontend := index.html app-worker.js app.js app.css manifest.webmanifest wasm_exec.js
src := main.go
exe := webflagchecker

all: $(dir) $(dir)/$(wasm) $(addprefix $(dir)/,$(frontend))

$(dir):
	mkdir -p $(dir)

$(dir)/$(wasm): $(src)
	GOARCH=wasm GOOS=js go build -o $@ $<

$(dir)/%: $(src)
	go build -o $(dir)/$(exe) $<
	cd $(dir) && ./$(exe)
	rm $(dir)/$(exe)

clean:
	rm -rf $(dir)




