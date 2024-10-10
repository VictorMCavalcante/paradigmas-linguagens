package main

import (
    "fmt"
)

type Carro struct {
    Marca  string
    Modelo string
    Ano    int
}

func main() {
    carro1 := Carro{"Toyota", "Ethios", 2020}
    carro2 := Carro{"Honda", "City", 2021}
    carro3 := Carro{"Ford", "Ka", 2019}

    fmt.Println(carro1)
    fmt.Println(carro2)
    fmt.Println(carro3)
}
