package config

import (
    "crypto/rand"
    "os"
    "strconv"
)

var Debug bool
var Port string
var Secret []byte
var Sessionname string
var DBservice string
var DBuser string
var DBpasswd string
var DBhost string
var DBport string
var DBname string
var DBdebug bool
var RedisURL string
var RedisPasswd string

func init() {
    loadenv()
    var err error
    debugstr, exists := os.LookupEnv("DEBUG")
    if !exists {
        Debug = false
    } else {
        Debug, err = strconv.ParseBool(debugstr)
        if err != nil {
            Debug = false
        }
    }
    dbdebugstr, exists := os.LookupEnv("DBDEBUG")
    if !exists {
        DBdebug = true
    } else {
        DBdebug, err = strconv.ParseBool(dbdebugstr)
        if err != nil {
            DBdebug = false
        }
    }
    Port = os.Getenv("PORT")
    Secret = make([]byte, 12)
    _, err = rand.Read(Secret)
    if err != nil {
        panic(err)
    }
    Sessionname = os.Getenv("SESSIONNAME")
    DBservice = os.Getenv("DBSERVICE")
    DBuser = os.Getenv("DBUSER")
    DBpasswd = os.Getenv("DBPASSWD")
    DBhost = os.Getenv("DBHOST")
    DBport = os.Getenv("DBPORT")
    DBname = os.Getenv("DBNAME")
    RedisURL = os.Getenv("REDISURL")
    RedisPasswd = os.Getenv("REDISPASSWD")
}
