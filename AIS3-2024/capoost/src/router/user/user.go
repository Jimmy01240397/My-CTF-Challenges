package user
import (
    "github.com/gin-gonic/gin"
    "github.com/gin-contrib/sessions"

    "capoost/middlewares/auth"
    "capoost/models/user"
    "capoost/utils/errutil"
)

var router *gin.RouterGroup

func Init(r *gin.RouterGroup) {
    router = r
    router.POST("/login", login)
    router.GET("/", auth.CheckSignIn, getuser)
    router.GET("/logout", auth.CheckSignIn, logout)
}

type userresult struct {
    Username string `json:"username"`
    IsAdmin bool `json:"isadmin"`
}

func getuser(c *gin.Context) {
    userdata, _ := c.Get("user")
    isAdmin, exist := c.Get("isAdmin")
    result := userresult{
        Username: userdata.(user.User).Username,
        IsAdmin: !(!exist || !isAdmin.(bool)),
    }
    c.JSON(200, result)
}

func login(c *gin.Context) {
    var userdata user.User
    c.BindJSON(&userdata)
    if !userdata.Login() {
        errutil.AbortAndError(c, &errutil.Err{
            Code: 401,
            Msg: "username or password incorrect",
        })
        return
    }
    session := sessions.Default(c)
    session.Set("user", userdata.Username)
    session.Save()
    c.String(200, "Login success")
}

func logout(c *gin.Context) {
    session := sessions.Default(c)
    session.Clear()
    session.Options(sessions.Options{MaxAge: -1})
    session.Save()
    c.String(200, "Logout success")
}
