//
//  FriendsTableViewCell.swift
//  Mood Tracker
//
//  Created by Yveslym on 10/3/17.
//  Copyright © 2017 Yveslym. All rights reserved.
//

import UIKit

class FriendsTableViewCell: UITableViewCell {

    @IBOutlet weak var fname: UILabel!
    @IBOutlet weak var lname: UILabel!
    @IBOutlet weak var currentMood: UILabel!
    @IBOutlet weak var previousMood: UILabel!
    
    @IBOutlet weak var myImage: UIImageView!
    
    
    
    
    
    override func awakeFromNib() {
        super.awakeFromNib()
        // Initialization code
    }

    override func setSelected(_ selected: Bool, animated: Bool) {
        super.setSelected(selected, animated: animated)

        // Configure the view for the selected state
    }

}
