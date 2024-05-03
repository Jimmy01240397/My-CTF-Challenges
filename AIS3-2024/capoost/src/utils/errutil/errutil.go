package errutil

import (
    "encoding/json"
    "github.com/gin-gonic/gin"
)

type Err struct {
    Code int `json:"code"`
    Msg interface{} `json:"msg"`
    Data interface{} `json:"data"`
}

func (e *Err) Error() string {
    b, _ := json.Marshal(e)
    return string(b)
}

func AbortAndError(c *gin.Context, err *Err) {
    c.Abort()
    c.JSON(err.Code, err)
}

func AbortAndStatus(c *gin.Context, code int) {
    c.Abort()
    c.Status(code)
}
