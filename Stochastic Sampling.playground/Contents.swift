//: Playground - noun: a place where people can play

import UIKit

// MARK: - Accessing Corpus
// Get the file path for the file "Horatius.txt" in the Playground bundle
let filePath = Bundle.main.path(forResource: "Horatius", ofType: "txt")

// Get the contentData
let contentData = FileManager.default.contents(atPath: filePath!)

// Get the string
let content = NSString(data: contentData!, encoding: String.Encoding.utf8.rawValue) as? String

// MARK: - Creating Distribution
func dictionaryHistogram(sourceText: String) -> [String]  {
    // Entire text that's splitted into key value pairs
    let entireSplittedText = sourceText.components(separatedBy: ", ")
    // Word dictionary 
    var wordDictionary: [String : Int] = [:]
    // Counter contains the int for the frequency
    var wordFrequency = 0
    // Loops through each word in the entire text 
    for word in entireSplittedText {
        // Going to every word and makes the Value 1 because it's the first word there.
        if wordDictionary.keys.contains(word) {
            // Making all words lowercased
            wordDictionary[word.lowercased()] += 1
        }
    }
    
    return entireSplittedText
}



