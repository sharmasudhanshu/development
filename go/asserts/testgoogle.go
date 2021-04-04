
package main

import (
"fmt"
	"net/http"
  "testing"
  "github.com/stretchr/testify/assert"
)

func myHandler(w http.ResponseWriter, r *http.Request) {
    w.Write([]byte(`hello world`))
}

func TestSomething(t *testing.T) {
  var a string = "Hello"
  var b string = "Hello"

  assert.Equal(t, a, b, "The two words should be the same.")
  assert.HTTPSuccess(t, myHandler, "POST", "http://www.google.com", nil)
 // assert.HTTPBodyContains(t, myHandler, "GET", "www.google.com", nil, "I'm Feeling Lucky")
 fmt.Println("from handler")
}
