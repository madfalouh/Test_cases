import unittest
from mockito import when

def calculate_bmi(height_feet, height_inches, weight , bmi_value=None) :
    if height_feet < 0 or height_inches < 0 or weight < 0:
        raise ValueError("Height and weight must be non-negative")
    total_height_inches = height_feet * 12 + height_inches
    weight_kg = weight * 0.45
    height_cm = total_height_inches * 0.025
   
    if bmi_value is not None:
        bmi = bmi_value
    else:
        bmi = weight_kg / (height_cm ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    return round(bmi, 1), category

class TestCalculateBMI(unittest.TestCase):
    
#part 1 
    def test_normal_weight(self):
        
        bmi, category = calculate_bmi(5, 6, 150 , bmi_value=18.5)
        
        self.assertEqual(category, "Normal weight")



    def test_underweight(self):
        bmi, category = calculate_bmi(5, 2, 90 ,  bmi_value=18.4)
   
        self.assertEqual(category, "Underweight")


#part 2 



    def test_overweight(self):
        bmi, category = calculate_bmi(6, 0, 200 ,  bmi_value=25)
     
        self.assertEqual(category, "Overweight")



    def test_normalweight(self):
        bmi, category = calculate_bmi(6, 0, 200,  bmi_value=24.9)
     
        self.assertEqual(category, "Normal weight")



#part 3

    def test_overweight(self):
        bmi, category = calculate_bmi(6, 0, 200 ,  bmi_value=25)
     
        self.assertEqual(category, "Overweight")


    def test_obese(self):
        bmi, category = calculate_bmi(5, 10, 250 ,  bmi_value=30.1)
        self.assertEqual(category, "Obese")


# interior 


    def test_overweight(self):
        bmi, category = calculate_bmi(6, 0, 200 ,  bmi_value=27)
     
        self.assertEqual(category, "Overweight")



  

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            calculate_bmi(5, -2, 150)
            



if __name__ == '__main__':
    unittest.main()
