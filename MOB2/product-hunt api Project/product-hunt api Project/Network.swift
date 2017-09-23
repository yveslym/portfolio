//
//  Network.swift
//  product-hunt api Project
//
//  Created by Yveslym on 9/23/17.
//  Copyright © 2017 Yveslym. All rights reserved.
//

import Foundation

struct Posts:Decodable {
    let comments_count: String
    let day: String
    let id: Int
    let product_state: String
    let tagline: String
    let category_id: String
    let created_at: String
}

enum netWorkError: Error {
    case cannotConnectToApi
    case CannotRetrieveData
    case cannotRetrieveApi
}


class Network{
    static func get_Network(withLink link:String!,Parameter param:[String:String], completionHandler: @escaping (Posts?,Error?)->Void){
        let url = URL(string: link)
        url?.appendingQueryParameters(param)
        var urlRequest = URLRequest(url: url!)
        urlRequest.addValue("application/json", forHTTPHeaderField: "Accept")
        urlRequest.addValue("api.producthunt.com", forHTTPHeaderField:"Host")
        urlRequest.addValue("Content-Type", forHTTPHeaderField: "application/json")
        urlRequest.addValue("Bearer  6055d5fc5fe82e4a2fe2628dc130d857efaa287e52491fc0b76ab1cfca018400 ", forHTTPHeaderField: "Authorization")
        
        URLSession.shared.dataTask(with: urlRequest){(data,reponse,error) in
            
            guard let data = data else {return completionHandler(nil, netWorkError.CannotRetrieveData)}
            guard reponse != nil else {return completionHandler(nil, netWorkError.cannotConnectToApi)}
            let decoder = JSONDecoder()
            guard let posts = try! decoder.decode(Posts?.self, from: data) else {return completionHandler(nil, netWorkError.cannotRetrieveApi)}
            return completionHandler(posts,nil)
            }
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


