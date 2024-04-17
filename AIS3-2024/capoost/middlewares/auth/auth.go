package auth

import (
//    "fmt"
    "github.com/gin-gonic/gin"
    "github.com/gin-contrib/sessions"

    "capoost/utils/errutil"
    "capoost/models/user"
)

func CheckSignIn(c *gin.Context) {
    if isSignIn, exist := c.Get("isSignIn"); !exist || !isSignIn.(bool) {
        errutil.AbortAndError(c, &errutil.Err{
            Code: 401,
            Msg: "You are not login.",
        })
    }
}

func CheckIsAdmin(c *gin.Context) {
    if isAdmin, exist := c.Get("isAdmin"); !exist || !isAdmin.(bool) {
        errutil.AbortAndError(c, &errutil.Err{
            Code: 405,
            Msg: "You are not admin.",
        })
    }
}

func CheckIsNotAdmin(c *gin.Context) {
    if isAdmin, exist := c.Get("isAdmin"); !(!exist || !isAdmin.(bool)) {
        errutil.AbortAndError(c, &errutil.Err{
            Code: 405,
            Msg: "This method is not available to admin.",
        })
    }
}

func AddMeta(c *gin.Context) {
    session := sessions.Default(c)
    username := session.Get("user")
    if username == nil {
        c.Set("isSignIn", false)
    } else {
        userdata, err := user.GetUser(username.(string))
        c.Set("user", userdata)
        if err != nil {
            c.Set("isSignIn", false)
        } else {
            c.Set("isSignIn", true)
            c.Set("isAdmin", userdata.ID == 1)
        }
    }
}
