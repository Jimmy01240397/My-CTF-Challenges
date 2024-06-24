package user

import (
    "log"
    "fmt"
    "encoding/base64"
    "crypto/rand"

    "capoost/utils/database"
    "capoost/utils/password"
)

type User struct {
    ID uint `gorm:"primaryKey" json:"-"`
    Username string `json:"username"`
    Password password.Password `json:"password"`
}

func init() {
    const adminname = "4dm1n1337"
    database.GetDB().AutoMigrate(&User{})

    if _, err := GetUser(adminname); err == nil {
        return
    }

    buf := make([]byte, 12)
    _, err := rand.Read(buf)
    if err != nil {
        log.Panicf("error while generating random string: %s", err)
    }
    User{
        //ID: 1,
        Username: adminname,
        Password: password.New(base64.StdEncoding.EncodeToString(buf)),
    }.Create()
}

func (a User) Equal(b User) bool {
    return a.Username == b.Username && a.Password == b.Password
}

func (user User) Login() bool {
    if user.Username == "" {
        return false
    }
    if _, err := GetUser(user.Username); err == nil {
        var loginuser User
        result := database.GetDB().Where(&user).First(&loginuser)
        return result.Error == nil
    }
    return user.Create() == nil
}

func GetUser(username string) (User, error) {
    var loginuser User
    result := database.GetDB().Where(&User{
        Username: username,
    }).First(&loginuser)
    return loginuser, result.Error
}

func (user User) Create() error {
    if user.Password == "" {
        return fmt.Errorf("Password can't be empty in create")
    }
    result := database.GetDB().Model(&User{}).Create(&user)
    return result.Error
}
