//
//  AddFriendViewController.swift
//  Mood Tracker
//
//  Created by Yveslym on 10/3/17.
//  Copyright © 2017 Yveslym. All rights reserved.
//

import UIKit

class AddFriendViewController: UIViewController,  UIPickerViewDelegate, UIPickerViewDataSource{
    func numberOfComponents(in pickerView: UIPickerView) -> Int {
        return count
    }
    
    func pickerView(_ pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int {
        return 1
    }
    
    
    let sexPicker = UIPickerView()
    let moodPicker = UIPickerView()
    
    var count: Int = 0
    @IBOutlet weak var fnameTF: UITextField!
    
    @IBOutlet weak var select: UIButton!
    @IBOutlet weak var lnameTF: UITextField!
    
    @IBOutlet weak var sexTF: UITextField!
    
    @IBOutlet weak var Mood: UITextField!
    
    weak var moodDelegate : MoodDelegate?
    weak var friendDelegate: FriendDelegate?
    override func viewDidLoad() {
        super.viewDidLoad()
        sexPicker.delegate = self
        sexPicker.dataSource = self
        
        moodPicker.dataSource = self
        moodPicker.delegate = self
        // Do any additional setup after loading the view.
    }

    @IBAction func DoneButton(_ sender: Any) {
        
        let newFirend = Friends(fname: fnameTF.text!, lname: lnameTF.text!, current: Mood.text!, previous: "")
        
        friendDelegate?.newFriend(friend: newFirend)
        select.isEnabled = false
    }
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    @IBAction func selectSex(_ sender: Any) {
        
       // let sex = ["men","girl"]
       
        
    }
    
    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
