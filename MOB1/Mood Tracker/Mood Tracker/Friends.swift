//
//  Friends.swift
//  Mood Tracker
//
//  Created by Yveslym on 10/3/17.
//  Copyright © 2017 Yveslym. All rights reserved.
//

import Foundation
class Friends: NSObject{
    
    let firstName: String?
    let lastName: String?
    var currentMood: String?
    var PreviousMood: String?
    let sex: String?
    
    init(fname: String, lname: String,current: String, previous: String, sex: String = "male") {
        self.firstName = fname
        self.lastName = lname
        self.currentMood = current
        self.PreviousMood = previous
        self.sex = sex
    }
    
    func setMood(mood: String){
        self.PreviousMood = self.currentMood
        self.currentMood = mood
    }
 
    
}

protocol FriendDelegate: class {
    func newFriend(friend: Friends)
}
