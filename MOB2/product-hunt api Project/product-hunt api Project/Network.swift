//
//  Network.swift
//  product-hunt api Project
//
//  Created by Yveslym on 9/23/17.
//  Copyright © 2017 Yveslym. All rights reserved.
//

import Foundation

struct Posts:Decodable {
    var name: String?
    var tagline: String?
    var votes: Int?
    var imageURL: String?
    var day: String?
    var postID : Int
//    let comments_count: String
//    let day: String
//    let id: Int
//    let product_state: String
//    let tagline: String
//    let category_id: String
//    let created_at: String
}
struct productHunt: Decodable{
    let posts = [Posts]()
}

enum netWorkError: Error {
    case cannotConnectToApi
    case CannotRetrieveData
    case cannotRetrieveApi
    case errorHappen
}
enum mykeys: String, CodingKey {
    case posts
}

class Network{
    static func get_Network(withLink link:String!,Parameter param:[String:String], completionHandler: @escaping ([Posts]?,Error?)->Void){
        var url = URL(string: link)
        let date = Date()
        let urlParams = ["search[featured]": "true",
                         "scope": "public",
                         "created_at": String(describing: date),
                         "per_page": "20"]
        url = url?.appendingQueryParameters(urlParams)
        print (url)
        
        var urlRequest = URLRequest(url: url!)
        urlRequest.addValue("application/json", forHTTPHeaderField: "Accept")
        urlRequest.addValue("api.producthunt.com", forHTTPHeaderField:"Host")
        urlRequest.addValue("Content-Type", forHTTPHeaderField: "application/json")
        urlRequest.addValue("Bearer 6055d5fc5fe82e4a2fe2628dc130d857efaa287e52491fc0b76ab1cfca018400 ", forHTTPHeaderField: "Authorization")
        urlRequest.httpMethod = "GET"
        
        let session = URLSession.shared
        session.dataTask(with: urlRequest) { (data,reponse,error) in
            
//            guard error == nil else { //print (error)
//                return completionHandler(nil, netWorkError.errorHappen)}
//            guard let data = data else {return completionHandler(nil, netWorkError.CannotRetrieveData)}
//            guard reponse != nil else {//print(error)
//                return completionHandler(nil, netWorkError.cannotConnectToApi)}
            let decoder = JSONDecoder()
            guard let product = try? decoder.decode(productHunt.self, from: data!) else {return completionHandler(nil, netWorkError.cannotRetrieveApi)}
            let posts = product.posts
         print (product)
            return completionHandler(posts,nil)
            }.resume()
    }
    
}


// URL  extension

extension URL {
    func appendingQueryParameters(_ parametersDictionary : Dictionary<String, String>) -> URL {
        let URLString : String = String(format: "%@?%@", self.absoluteString, parametersDictionary.queryParameters)
        return URL(string: URLString)!
    }
    // This is formatting the query parameters with an ascii table reference therefore we can be returned a json file
}

protocol URLQueryParameterStringConvertible {
    var queryParameters: String {get}
}


extension Dictionary : URLQueryParameterStringConvertible {
    /**
     This computed property returns a query parameters string from the given NSDictionary. For
     example, if the input is @{@"day":@"Tuesday", @"month":@"January"}, the output
     string will be @"day=Tuesday&month=January".
     @return The computed parameters string.
     */
    var queryParameters: String {
        var parts: [String] = []
        for (key, value) in self {
            let part = String(format: "%@=%@",
                              String(describing: key).addingPercentEncoding(withAllowedCharacters: .urlQueryAllowed)!,
                              String(describing: value).addingPercentEncoding(withAllowedCharacters: .urlQueryAllowed)!)
            parts.append(part as String)
        }
        return parts.joined(separator: "&")
    }
    
}