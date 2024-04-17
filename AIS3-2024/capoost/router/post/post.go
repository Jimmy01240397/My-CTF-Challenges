package post
import (
    "path"
    "strconv"
    "text/template"
    "os/exec"
    "os"
    "regexp"
    "errors"
    "bytes"
    "strings"

    "github.com/gin-gonic/gin"

    "capoost/middlewares/auth"
    "capoost/models/user"
    "capoost/models/post"
    "capoost/utils/errutil"
    "capoost/utils/database"
)

type page struct {
    Data string `json:"data"`
    Count int `json:"count"`
    Percent int `json:"percent"`
}

var router *gin.RouterGroup

func Init(r *gin.RouterGroup) {
    router = r
    router.POST("/create", auth.CheckSignIn, auth.CheckIsNotAdmin, create)
    router.GET("/list", auth.CheckSignIn, list)
    router.GET("/read", auth.CheckSignIn, read)
}

func create(c *gin.Context) {
    userdata, _ := c.Get("user")
    postdata := post.Post{
        Owner: userdata.(user.User),
    }
    err := c.ShouldBindJSON(&postdata)
    if err != nil || postdata.Title == "" {
        errutil.AbortAndError(c, &errutil.Err{
            Code: 400,
            Msg: "Invalid Post",
        })
        return
    }
    reg := regexp.MustCompile(`[^a-zA-Z0-9]`)
    postdata.Template = reg.ReplaceAllString(postdata.Template, "")
    if _, err := os.Stat(path.Clean(path.Join("./template", postdata.Template))); 
        path.Clean(path.Join("./template", postdata.Template)) == path.Clean("./template") ||
        errors.Is(err, os.ErrNotExist) {
        errutil.AbortAndError(c, &errutil.Err{
            Code: 400,
            Msg: "Invalid Post",
        })
        return
    }
    postdata.Create()

    c.String(200, "Post success")
}

func list(c *gin.Context) {
    posts, err := post.GetAllPosts()
    if err != nil {
        panic(err)
    }
    c.JSON(200, posts)
}

func read(c *gin.Context) {
    postid, err := strconv.Atoi(c.DefaultQuery("id", "0"))
    if err != nil {
        errutil.AbortAndError(c, &errutil.Err{
            Code: 400,
            Msg: "Invalid ID",
        })
    }
    nowpost, err := post.GetPost(uint(postid))
    if err != nil {
        errutil.AbortAndError(c, &errutil.Err{
            Code: 400,
            Msg: "Invalid ID",
        })
    }
    t := template.New(nowpost.Template)
    if nowpost.Owner.ID == 1 {
        t = t.Funcs(template.FuncMap{
            "G1V3m34Fl4gpL34s3": readflag,
        })
    }
    t = template.Must(t.ParseFiles(path.Join("./template", nowpost.Template)))
    b := new(bytes.Buffer)
    if err = t.Execute(b, nowpost.Data); err != nil {
        panic(err)
    }
    nowpost.Count++
    sum := 0
    posts, _ := post.GetAllPosts()
    for _, now := range posts {
        if nowpost.ID == now.ID {
            sum += nowpost.Count
        } else {
            sum += now.Count
        }
    }
    var percent int 
    if sum != 0 {
        percent = (nowpost.Count * 100) / sum
    } else {
        errutil.AbortAndError(c, &errutil.Err{
            Code: 500,
            Msg: "Sum of post count can't be 0",
        })
    }
    if strings.Contains(b.String(), "AIS3") {
        errutil.AbortAndError(c, &errutil.Err{
            Code: 403,
            Msg: "Flag deny",
        })
    }
    nowpage := page{
        Data: b.String(),
        Count: nowpost.Count,
        Percent: percent,
    }
    c.JSON(200, nowpage)
    database.GetDB().Save(&nowpost)
}

func readflag() string {
    out, _ := exec.Command("/readflag").Output()
    return strings.Trim(string(out), " \n\t")
}
