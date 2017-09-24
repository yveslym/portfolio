//
//  ViewController.swift
//  product-hunt api Project
//
//  Created by Yveslym on 9/23/17.
//  Copyright © 2017 Yveslym. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        let date = Date()
         var link =  "https://api.producthunt.com/v1/posts"
        let param = ["search[featured]": "true",
                         "scope": "public",
                         "created_at": String(describing: date),
                         "per_page": "20"]
        Network.get_Network(withLink: link, Parameter: param, completionHandler: {(post, error) in
          
            print(post)
        })
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

