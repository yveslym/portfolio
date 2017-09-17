//: Playground - noun: a place where people can play

import UIKit
import Foundation
import PlaygroundSupport

var str = "Hello, playground"

struct house_listing: Decodable{
    let bathrooms: Double
    let bedrooms: Int
    let beds: Int
    let city: String
    let id: Int
    let name: String
}

struct house_pricing: Decodable{
    let available: Bool
    let guests: Int
    let night_price: Int
}
struct house: Decodable{
    let listing: house_listing
    let pricing_quote: house_pricing
}

struct search_result: Decodable{
    let index: [house]
}


let link = "https://api.airbnb.com/v2/search_results?key=915pw2pnf4h1aiguhph5gc5b2"
let url = URL(string: link)

URLSession.shared.dataTask(with: url!){(data,reponse,err) in
    guard let data = data else {return}
    do{
        let decoder = JSONDecoder()
        let search_results = try! decoder.decode(search_result.self, from: data)
    }
    
}










