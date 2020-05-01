package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)

	binString := "1101001010"

	fmt.Println("The Final Game. Play this to free yourselves.")

	var answer string
	fmt.Println("Give me the code I seek and then you shall free yourselves!")
	fmt.Print("> ")
	answer, _ = reader.ReadString('\n')
	answer = strings.TrimSpace(answer)

	for answer != binString {
		fmt.Println("NOPE! \nListen to the code and tell it to me in a language that I can understand.")
		fmt.Print("> ")
		answer, _ = reader.ReadString('\n')
		answer = strings.TrimSpace(answer)
	}

	fmt.Println("Good job! You have satisfied me! Now, go take a team selfie to rejoice this moment!")

	fmt.Println("Press any key to continue");
	answer, _ = reader.ReadString('\n')
}
