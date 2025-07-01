package main

import (
    "math/bits"
    "log"
    "github.com/maxence-charriere/go-app/v10/pkg/app"
    "encoding/binary"
)

type flagpagecomposer struct {
    app.Compo
    flag string
    result string
}

var key = uint32(0xfd9ea72d)
var ans = [5]uint64{0x69282a668aef666a,0x633525f4d7372337,0x9db9a5a0dcc5dd7d,0x9833afafb8381a2f,0x6fac8c8726464726}

func main() {
    // Components routing:
    app.Route("/", flagpage)
    app.RunWhenOnBrowser()

    err := app.GenerateStaticWebsite(".", &app.Handler{
        Name:        "Flag Checker",
        Description: "Flag Checker",
    })

    if err != nil {
        log.Fatal(err)
    }
}

func flagpage() app.Composer {
    return &flagpagecomposer{}
}

func (c *flagpagecomposer) Render() app.UI {
    return app.Div().Body(
        app.H1().Body(
            app.Text("This is a web flag checker. Give me a flag."),
        ),
        app.P().Body(
            app.Input().Type("text").Value(c.flag).Placeholder("Input a flag").OnChange(c.ValueTo(&c.flag)),
            app.Button().Text("check").OnClick(func(ctx app.Context, e app.Event) {
                if flagchecker(c.flag) {
                    c.result = "Success"
                } else {
                    c.result = "Wrong flag"
                }
                ctx.Dispatch(func(app.Context) {})
            }),
        ),
        app.P().Body(
            app.Text(c.result),
        ),
    )
}

func flagchecker(nowflag string) bool {
    if len(nowflag) != 40 {
        return false
    }
    data := []byte(nowflag)
    for i := 0; i < 5; i++ {
        now := binary.LittleEndian.Uint64(data[i*8:(i+1)*8])
        now = bits.RotateLeft64(now, int((key>>(i*6)) & 0b111111))
        if now != ans[i] {
            return false
        }
    }
    return true
}

