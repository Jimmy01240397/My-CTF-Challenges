package router
import (
    "github.com/gin-gonic/gin"

//    "capoost/middlewares/auth"
    "capoost/router/user"
    "capoost/router/template"
    "capoost/router/post"
)

var router *gin.RouterGroup

func Init(r *gin.RouterGroup) {
    router = r
    user.Init(router.Group("/user"))
    template.Init(router.Group("/template"))
    post.Init(router.Group("/post"))
}


