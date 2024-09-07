import React, { useState, useEffect } from "react";
import axios from "axios";
import styled from "styled-components";

interface ViolationData {
  violation_type_code: string[];
  street: string[];
  boro: string[];
  house_number: string[];
}

// Styled Components for a prettier UI
const Container = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f4f7f6;
`;

const FormWrapper = styled.div`
  background-color: white;
  padding: 40px;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  max-width: 500px;
  width: 100%;
`;

const Title = styled.h1`
  font-size: 24px;
  margin-bottom: 20px;
  text-align: center;
  color: #333;
`;

const Form = styled.form`
  display: flex;
  flex-direction: column;
`;

const FieldGroup = styled.div`
  display: flex;
  flex-direction: column;
  margin-bottom: 15px;
`;

const Label = styled.label`
  font-size: 14px;
  margin-bottom: 5px;
  color: #555;
`;

const Select = styled.select`
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 14px;
  width: 100%;
`;

const Input = styled.input`
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 14px;
  width: 100%;
`;

const Button = styled.button`
  padding: 12px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s ease;

  &:hover {
    background-color: #45a049;
  }
`;

const Result = styled.div`
  background-color: #e7f3e7;
  padding: 15px;
  margin-top: 20px;
  border-radius: 5px;
  font-size: 16px;
  color: #333;
  text-align: center;
`;

const App: React.FC = () => {
  const [violationData, setViolationData] = useState<ViolationData>({
    violation_type_code: [],
    street: [],
    boro: [],
    house_number: [],
  });
  const [formData, setFormData] = useState({
    violation_type_code: "",
    street: "",
    boro: "",
    house_number: "",
    block: "",
  });
  const [predictedCategory, setPredictedCategory] = useState<string>("");

  useEffect(() => {
    // Fetch available violation data (violation_type_code and street)
    axios
      .get("http://localhost:5000/violation-data")
      .then((response) => {
        setViolationData(response.data);
      })
      .catch((error) => {
        console.error("Error fetching violation data:", error);
      });
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        "http://localhost:5000/predict",
        formData
      );
      setPredictedCategory(response.data.violation_category);
    } catch (error) {
      console.error("Error predicting violation category:", error);
    }
  };

  const handleInputChange = (
    e: React.ChangeEvent<HTMLSelectElement | HTMLInputElement>
  ) => {
    const { name, value } = e.target;
    setFormData((prevState) => ({ ...prevState, [name]: value }));
  };

  return (
    <Container>
      <FormWrapper>
        <Title>Violation Category Prediction</Title>
        <Form onSubmit={handleSubmit}>
          <FieldGroup>
            <Label htmlFor="violation_type_code">Violation Type Code:</Label>
            <Select
              id="violation_type_code"
              name="violation_type_code"
              value={formData.violation_type_code}
              onChange={handleInputChange}
              required
            >
              <option value="">Select Violation Type</option>
              {violationData.violation_type_code.map((code, index) => (
                <option key={index} value={code}>
                  {code}
                </option>
              ))}
            </Select>
          </FieldGroup>

          <FieldGroup>
            <Label htmlFor="street">Street:</Label>
            <Select
              id="street"
              name="street"
              value={formData.street}
              onChange={handleInputChange}
              required
            >
              <option value="">Select Street</option>
              {violationData.street.map((street, index) => (
                <option key={index} value={street}>
                  {street}
                </option>
              ))}
            </Select>
          </FieldGroup>

          <FieldGroup>
            <Label htmlFor="boro">Borough:</Label>
            <Select
              id="boro"
              name="boro"
              value={formData.boro}
              onChange={handleInputChange}
              required
            >
              <option value="">Select Borough</option>
              {violationData.boro.map((boro, index) => (
                <option key={index} value={boro}>
                  {boro}
                </option>
              ))}
            </Select>
          </FieldGroup>

          <FieldGroup>
            <Label htmlFor="house_number">House Number:</Label>
            <Select
              id="house_number"
              name="house_number"
              value={formData.house_number}
              onChange={handleInputChange}
              required
            >
              <option value="">Select House Number</option>
              {violationData.house_number.map((house, index) => (
                <option key={index} value={house}>
                  {house}
                </option>
              ))}
            </Select>
          </FieldGroup>

          <FieldGroup>
            <Label htmlFor="block">Block:</Label>
            <Input
              type="text"
              id="block"
              name="block"
              value={formData.block}
              onChange={handleInputChange}
              required
            />
          </FieldGroup>

          <Button type="submit">Predict Violation Category</Button>
        </Form>

        {predictedCategory && (
          <Result>
            <h2>Predicted Violation Category:</h2>
            <p>{predictedCategory}</p>
          </Result>
        )}
      </FormWrapper>
    </Container>
  );
};

export default App;
