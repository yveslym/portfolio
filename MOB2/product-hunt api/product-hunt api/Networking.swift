//
//  Networking.swift
//  product-hunt api
//
//  Created by Yveslym on 9/27/17.
//  Copyright © 2017 Yveslym. All rights reserved.
//

import Foundation


struct Product {
    // Modeling the properties we want back from the JSON Data
    var name: String?
    var tagline: String?
    var votes: Int?
    var imageURL: String?
    var day: String?
    var postID : Int
    
    // What is the point of initalizing the data?
    init(name: String?, tagline: String?, votesCount: Int?, imageURL: String?, day: String?, postID: Int) {
        self.name = name
        self.tagline = tagline
        self.votes = votesCount
        self.imageURL = imageURL
        self.day = day
        self.postID = postID
    }
}

extension Product: Decodable {
    // Creating  our case statements to iterate over the data in the JSON File
    
    enum additionalKeys: String, CodingKey {
        // Creating case statements that are nested within the posts list embedded with dictionaries
        case name
        case tagline
        case votes = "votes"
        case day
        case thumbnail
        case postID = "id"
    }
    
    enum  thubnailImage: String, CodingKey {
        case imageURL = "image_url"
    }
    
    init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: additionalKeys.self)
        let votes = try container.decodeIfPresent(Int.self, forKey: .votes) ?? 0
        let name = try container.decodeIfPresent(String.self, forKey: .name)
        let tagline = try container.decodeIfPresent(String.self, forKey: .tagline)
        let day = try container.decodeIfPresent(String.self, forKey: .day) ?? "The day is not here"
        let postID = try container.decode(Int.self, forKey: .postID)
        let thumbnailContainer = try? container.nestedContainer(keyedBy: thubnailImage.self, forKey: .thumbnail)
        if let _ = thumbnailContainer {
            let imageURL = try thumbnailContainer?.decodeIfPresent(String.self, forKey: .imageURL) ?? "No Image"
            self.init(name: name, tagline: tagline, votesCount: votes, imageURL: imageURL, day: day, postID: postID)
            return
        }
        self.init(name: name, tagline: tagline, votesCount: votes, imageURL: "image", day: day, postID: postID)
    }
}











//struct Product: Decodable {
//    var name: String?
//    var tagline: String?
//    var votes: Int?
//    var imageURL: String?
//    var id: Int?
//
//    init(name: String, tagline: String, votes: Int, imageURL: String, id: Int) {
//        self.name = name
//        self.tagline = tagline
//        self.votes = votes
//        self.imageURL = imageURL
//        self.id = id
//    }
//}
//
//struct comment{
//    var body: String?
//    init(body: String) {
//        self.body = body
//    }
//}
//
//extension Product {
//
//    enum ProductKey: String, CodingKey {
//        case name
//        case tagline
//        case votes
//        case imageURL
//    }
//
//
//}
//
//// root path
//// base url
//enum Route{
//    case post
//    case comments (postID: String)
//    case me
//  //path
//    func path() -> String{
//        switch self {
//        case .post: return "posts"
//        case .comments: return "cmments"
//        case .me: return "users"
//        }
//    }
//
//// URL parameer - query parameter(addition to url)
//
//    func urlParameters() ->[String:String]{
//        switch self {
//        case .post: return [:]
//        case let .comments(postID):
//            return ["search[post_id]": postID, "page":"2"]
//
//        case .me:
//            return [:]
//        }
//    }
//// headers
//
// // body
//
//    // header:
//}




















