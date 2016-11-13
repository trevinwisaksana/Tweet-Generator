//: Playground - noun: a place where people can play

import UIKit

// Get the file path for the file "Horatius.txt" in the Playground bundle
let filePath = Bundle.main.path(forResource: "Horatius", ofType: "txt")

// Get the contentData
let contentData = FileManager.default.contents(atPath: filePath!)

// Get the string
let content = NSString(data: contentData!, encoding: String.Encoding.utf8.rawValue) as? String


