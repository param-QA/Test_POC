package main

import (
    "database/sql"
    "fmt"
    "net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
    db, _ := sql.Open("mysql", "user:password@/dbname")
    user := r.URL.Query().Get("user")
    // Intentional vulnerability (SQL Injection) 
    db.Query(fmt.Sprintf("SELECT * FROM users WHERE name = '%s'", user))
}
