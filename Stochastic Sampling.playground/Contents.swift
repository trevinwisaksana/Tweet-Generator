//: Playground - noun: a place where people can play

import UIKit

// MARK: - Creating Distribution
func dictionaryHistogram(sourceText: String) -> [String : Int]  {
    // Entire text that's splitted into key value pairs
    let entireSplittedText = sourceText.components(separatedBy: " ")
    // Word dictionary
    var wordDictionary = [String : Int]()
    // Loops through each word in the entire text
    for word in entireSplittedText {
        // keyValue is the frequency value
        var keyValue = 0
        // Going to every word and makes the Value 1 because it's the first word there.
        if wordDictionary.keys.contains(word) {
            // Making all words lowercased
            keyValue = wordDictionary[word]! + 1
            wordDictionary.updateValue(keyValue, forKey: word)
        } else {
            wordDictionary[word] = 1
        }
    }
    
    return wordDictionary
}

// MARK: - Accessing Corpus
// Get the file path for the file "Fish.txt" in the Playground bundle
if let filePath = Bundle.main.path(forResource: "Fish", ofType: "txt") {
    // Get the contentData
    let contentData = FileManager.default.contents(atPath: filePath)
    // Get the string
    let content = NSString(data: contentData!, encoding: String.Encoding.utf8.rawValue) as? String
    // Using the dictionaryHistogram function to process the array into a histogram
    dictionaryHistogram(sourceText: content!)
}






