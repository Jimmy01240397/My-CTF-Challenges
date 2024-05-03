package post

import (
    "fmt"
    "reflect"
    "encoding/json"
    "database/sql/driver"

    "gorm.io/datatypes"

    "capoost/models/user"
    "capoost/utils/database"
)

type PostDataMap map[string]any

type Post struct {
    ID uint `gorm:"primaryKey" json:"id"`
    Title string `json:"title"`
    OwnerID uint `json:"-"`
    Owner user.User `gorm:"foreignKey:OwnerID" json:"owner"`
    Template string `json:"template"`
    Data PostDataMap `json:"data"`
    Count int `json:"count"`
}

type postjson struct {
    ID uint `json:"id"`
    Title string `json:"title"`
    Owner string `json:"owner"`
    Template string `json:"template"`
    Data PostDataMap `json:"data"`
    Count int `json:"count"`
}

func init() {
    database.GetDB().AutoMigrate(&Post{})
}

func GetPost(id uint) (Post, error) {
    var postdata Post
    result := database.GetDB().Model(&Post{}).Preload("Owner").Where("id = ?", id).First(&postdata)
    return postdata, result.Error
}

func GetAllPosts() ([]Post, error) {
    var postdatas []Post
    result := database.GetDB().Model(&Post{}).Preload("Owner").Find(&postdatas)
    return postdatas, result.Error
}

func (post Post) Create() error {
    result := database.GetDB().Model(&Post{}).Create(&post)
    return result.Error
}

func (c Post) MarshalJSON() ([]byte, error) {
    data := postjson{
        ID: c.ID,
        Title: c.Title,
        Owner: c.Owner.Username,
        Template: c.Template,
        Data: c.Data,
        Count: c.Count,
    }
    return json.Marshal(data)
}

func (c *Post) UnmarshalJSON(b []byte) error {
    var tmp postjson
    err := json.Unmarshal(b, &tmp)
    if err != nil {
        return err
    }
    c.ID = tmp.ID
    c.Title = tmp.Title
    if tmp.Owner != "" {
        if owner, err := user.GetUser(tmp.Owner); err == nil {
            c.OwnerID = owner.ID
            c.Owner = owner
        }
    }
    c.Template = tmp.Template
    c.Data = tmp.Data
    c.Count = tmp.Count
    return nil
}

func (c PostDataMap) MarshalJSON() ([]byte, error) {
    return json.Marshal(map[string]any(c))
}

func (c *PostDataMap) UnmarshalJSON(b []byte) error {
    var tmp map[string]any
    err := json.Unmarshal(b, &tmp)
    if err != nil {
        return err
    }
    *c = PostDataMap(tmp)
    return nil
}

func (c *PostDataMap) Scan(value interface{}) (err error) {
    if val, ok := value.(datatypes.JSON); ok {
        err = json.Unmarshal([]byte(val), c)
        if err != nil {
            return
        }
    } else if val, ok := value.(json.RawMessage); ok {
        err = json.Unmarshal([]byte(val), c)
        if err != nil {
            return
        }
    } else if val, ok := value.([]byte); ok {
        err = json.Unmarshal([]byte(val), c)
        if err != nil {
            return
        }
    } else {
        err = fmt.Errorf("sql: unsupported type %s", reflect.TypeOf(value))
    }
    return
}

func (c PostDataMap) Value() (driver.Value, error) {
    data, err := json.Marshal(map[string]any(c))
    return datatypes.JSON(data), err
}
