package main

import (
	"encoding/json"
	"fmt"
)

type Bird struct {
	Species     string `json:"birdType"`
	Description string `json:"what it does"`
}

func main() {
	birdJson := `{"birds":{"pigeon":"likes to perch on rocks","eagle":"bird of prey"},"animals":{"wolf":"animals to howl on rocks","leoperd":"animals of prey"}}`
	var result map[string]interface{}  //we create a map of strings to empty interfaces
	json.Unmarshal([]byte(birdJson), &result)

	// The object stored in the "birds" key is also stored as 
	// a map[string]interface{} type, and its type is asserted from
	// the interface{} type
	birds := result["birds"].(map[string]interface{})

	for key, value := range birds {
		// Each value is an interface{} type, that is type asserted as a string
		fmt.Println(key, value.(string))
	}
	//pigeon likes to perch on rocks
	//eagle bird of prey



	animalz := result["animals"].(map[string]interface{})

	for key, value := range animalz {
		// Each value is an interface{} type, that is type asserted as a string
		fmt.Println(key, value.(string))
	}
	//wolf animals to howl on rocks
	//leoperd animals of prey

}


