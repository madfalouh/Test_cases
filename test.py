import unittest


def calculate_bmi(height_feet, height_inches, weight ) :
    if height_feet < 0 or height_inches < 0 or weight < 0:
        raise ValueError("Height and weight must be non-negative")
    total_height_inches = height_feet * 12 + height_inches
    weight_kg = weight * 0.45
    height_cm = total_height_inches * 0.025
    
    bmi = weight_kg / (height_cm ** 2)
    bmi = round(bmi,1)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
   
    return bmi, category

class TestCalculateBMI(unittest.TestCase):
    
#Domain 1 



      #bmi 18.5
    def test_normal_weight_1(self):
        
        bmi, category = calculate_bmi(5 , 2 , 98.75)
        
        self.assertEqual(category, "Normal weight")


  #bmi 18.4
    def test_underweight_2(self):
        bmi, category = calculate_bmi(5, 2, 98.22 )
        self.assertEqual(category, "Underweight")
        
  #bmi 17
    def test_underweight_3(self):
        bmi, category = calculate_bmi(5, 2, 90.75 )
        
        self.assertEqual(category, "Underweight")


#Domain 2 


  #bmi 25
    def test_overweight_4(self):
        bmi, category = calculate_bmi(6, 0, 180)
        
        self.assertEqual(category, "Overweight")

  #bmi 18.5
    def test_normalweight_5(self):
        bmi, category = calculate_bmi(5 , 2 , 98.75)
     
        self.assertEqual(category, "Normal weight")
        
  #bmi 20
    def test_normalweight_6(self):
        bmi, category = calculate_bmi(6, 0, 144)
     
        self.assertEqual(category, "Normal weight")
        

  #bmi 24.9
    def test_normalweight_7(self):
        bmi, category = calculate_bmi(6, 0, 179.26)
     
        self.assertEqual(category, "Normal weight")


  #bmi 18.4
    def test_normalweight_8(self):
        bmi, category = calculate_bmi(5, 2, 98.22)
        
        self.assertEqual(category, "Underweight")



#DOmain 3 

  #bmi 25
    def test_overweight_9(self):
        bmi, category = calculate_bmi(6, 0, 180 )
     
        self.assertEqual(category, "Overweight")


  #bmi 27
    def test_overweight_10(self):
        bmi, category = calculate_bmi(5, 9, 181.11 )
     
        self.assertEqual(category, "Overweight")
        

  #bmi 29.9
    def test_normalweight_11(self):
        bmi, category = calculate_bmi(6, 0, 215.26)
     
        self.assertEqual(category, "Overweight")

  #bmi 30
    def test_obese_12(self):
        bmi, category = calculate_bmi(5, 10, 204.15 )
        self.assertEqual(category, "Obese")

  #bmi 24.9
    def test_normalweight_13(self):
        bmi, category = calculate_bmi(6, 0, 179.26)
     
        self.assertEqual(category, "Normal weight")
        


# Domain 4  

  #bmi 30
    def test_overweight_14(self):
        bmi, category = calculate_bmi(5, 10, 204.15 )
     
        self.assertEqual(category, "Obese")
        

  #bmi 32
    def test_overweight_15(self):
        bmi, category = calculate_bmi(6, 0, 230.4 )
        self.assertEqual(category, "Obese")

  #bmi 29.9
    def test_normalweight_16(self):
        bmi, category = calculate_bmi(6, 0, 215.26)

        self.assertEqual(category, "Overweight")

  

    def test_negative_input_17(self):
        with self.assertRaises(ValueError):
            calculate_bmi(5, -2, 150)
            



if __name__ == '__main__':
    unittest.main()
