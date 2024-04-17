package template
import (
    "os"
    "path"
    "regexp"
    "github.com/gin-gonic/gin"

    "capoost/middlewares/auth"
    "capoost/utils/errutil"
)

var router *gin.RouterGroup

func init() {
    os.MkdirAll("./template", os.ModePerm)
}

func Init(r *gin.RouterGroup) {
    router = r
    router.POST("/upload", auth.CheckSignIn, auth.CheckIsAdmin, upload)
    router.GET("/list", auth.CheckSignIn, list)
    router.GET("/read", auth.CheckSignIn, read)
}

func upload(c *gin.Context) {
    reg := regexp.MustCompile(`[^a-zA-Z0-9]`)
    template := c.PostForm("template")
    name := reg.ReplaceAllString(c.PostForm("name"), "")
    f, err := os.Create(path.Clean(path.Join("./template", name)))
    if err != nil {
        panic(err)
    }
    _, err = f.WriteString(template)
    if err != nil {
        panic(err)
    }
    c.String(200, "Upload success")
}

func list(c *gin.Context) {
    tmpls, err := os.ReadDir("./template")
    if err != nil {
        panic(err)
    }
    result := make([]string, len(tmpls))
    for i, tmpl := range tmpls {
        result[i] = tmpl.Name()
    }
    c.JSON(200, result)
}

func read(c *gin.Context) {
    name := c.Query("name")
    if name == "" {
        errutil.AbortAndError(c, &errutil.Err{
            Code: 400,
            Msg: "Bad name",
        })
        return
    }
    c.File(path.Join("./template", name))
}
