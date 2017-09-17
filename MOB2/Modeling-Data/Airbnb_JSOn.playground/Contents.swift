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

let link = "https://api.airbnb.com/v2/search_results"
let url = URL(string: link)

URLSession.shared.dataTask(with: url!){(data,reponse,err) in
    
    guard let data = data else {return}
//
    do{
    let search_results = try
        JSONDecoder().decode(search_result.self, from: data)
   }
}
