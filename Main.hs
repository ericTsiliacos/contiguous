import           Test.Hspec

subarray :: [Int] -> Int
subarray array@(_:xs) =
  let
    length' = length array
  in
      if contiguous array length' then
        length'
      else
        max (subarray xs) (subarray $ init array)

contiguous :: [Int] -> Int -> Bool
contiguous xs length' = maximum xs - minimum xs == length' - 1

main :: IO ()
main = hspec $
  describe "Subarray" $ do
    it "returns 1 for an array of 1 element" $
      subarray [1] `shouldBe` 1
    it "returns 2 for a continguous array of 2 elements" $
      subarray [1, 2] `shouldBe` 2
    it "returns 1 for a discontinguous array of 2 elements" $
      subarray [1, 3] `shouldBe` 1
    it "returns 2 for a discontinguous array from the left of 3 elements" $
      subarray [4, 1, 2] `shouldBe` 2
    it "returns 2 for a discontinguous array from the right of 3 elements" $
      subarray [1, 2, 4] `shouldBe` 2
