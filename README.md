# calories_calc

# Calories Calculator App

A Python-based application that analyzes food images and provides detailed nutritional information using OpenAI's Assistant API with vision capabilities.

## Features

- **Image-based Food Analysis**: Upload food images and get detailed nutritional breakdown
- **Comprehensive Nutrition Data**: Provides calories, carbohydrates, protein, fat, fiber, sugars, and sodium content
- **OpenAI Assistant Integration**: Uses OpenAI's latest Assistant API v2 with vision capabilities
- **Multiple Food Detection**: Identifies and analyzes multiple food items in a single image
- **Total Nutrition Calculation**: Aggregates nutritional values for complete meal analysis

## Project Structure

```
calories_calc2/
├── basic_calories_calc.py     # Main application file
├── config.json               # Configuration file with API keys
├── requirements.txt          # Python dependencies
├── duck.jpg                 # Sample food image
├── Blueberry-Smoothie.jpg   # Sample food image
├── clipboard-image.png      # Sample food image
├── deputydev_prompt.txt     # Prompt to modify the project
└── README.md               # This file
```

## Prerequisites

- Python 3.11
- OpenAI API key
- OpenAI Assistant ID (pre-configured in config.json)

## Installation

1. **Clone or download the project**
   ```bash
   cd calories_calc2
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify configuration**
   - The `config.json` file should contain your OpenAI API key and assistant ID

## Usage

### Basic Usage

1. **Prepare your food image**
   - Ensure you have a food image in a supported format (PNG, JPG, JPEG)
   - Update the `image_path` variable in `basic_calories_calc.py` to point to your image

2. **Run the application**
   ```bash
   python basic_calories_calc.py
   ```

3. **View results**
   - The application will analyze the image and display detailed nutritional information
   - Results include individual food item analysis and total nutritional values

### Customizing Image Path

Edit line 47 in `basic_calories_calc.py`:
```python
image_path = "path/to/your/food/image.jpg"
```

### Expected Output Format

The application returns nutrition data in the following JSON structure:

```json
{
  "is_food_item": true,
  "food_items_detected": ["white bread", "American cheese", "butter", "egg"],
  "detailed_nutrition_value": [
    {
      "food_name": "white bread",
      "quantity": "2 slices (about 56g)",
      "calories": "140 kcal",
      "carbohydrates": "28 g",
      "sugars": "3 g",
      "fiber": "1 g",
      "protein": "4 g",
      "fat": "2 g",
      "sodium": "260 mg"
    }
  ],
  "total_nutrition_value": {
    "calories": "430 kcal",
    "carbohydrates": "33 g",
    "sugars": "6 g",
    "fiber": "1 g",
    "protein": "16 g",
    "fat": "28 g",
    "sodium": "1220 mg"
  }
}
```

## How It Works

1. **Image Processing**: The application encodes the food image and uploads it to OpenAI
2. **AI Analysis**: Uses OpenAI's Assistant API with vision capabilities to identify food items
3. **Nutrition Calculation**: The AI assistant analyzes each detected food item and calculates nutritional values
4. **Result Aggregation**: Combines individual food nutrition data into total meal nutrition

## Configuration

### config.json Structure
```json
{
  "openai_api_key": "your-openai-api-key-here",
  "assistant_id": "your-assistant-id-here"
}
```

### Environment Variables
The application automatically sets the `OPENAI_API_KEY` environment variable from the config file.

## Dependencies

- **openai==1.68.2**: OpenAI API client
- **Pillow==11.1.0**: Image processing library
- **python-dotenv>=1.0.0**: Environment variable management
- **streamlit==1.45.1**: Web app framework (for future enhancements)

## Troubleshooting

### Common Issues

1. **Config file not found**
   - Ensure `config.json` exists in the project directory
   - Verify the file contains valid JSON with required keys

2. **API key issues**
   - Check that your OpenAI API key is valid and has sufficient credits
   - Ensure the API key has access to the Assistant API

3. **Image path errors**
   - Verify the image path exists and is accessible
   - Ensure the image is in a supported format (PNG, JPG, JPEG)

4. **Assistant ID errors**
   - The assistant ID is pre-configured and should work with the provided configuration
   - If issues persist, contact the project maintainer

## Sample Images

The project includes sample food images for testing:
- `duck.jpg` - Sample duck dish
- `Blueberry-Smoothie.jpg` - Blueberry smoothie
- `clipboard-image.png` - General food image

## Notes

- The application uses OpenAI's Assistant API v2 with vision capabilities
- Nutrition values are estimates based on AI analysis
- For production use, consider implementing error handling and input validation
- The assistant is pre-trained to provide detailed nutritional analysis

## Support

For issues or questions related to this application, please check the configuration and ensure all dependencies are properly installed.
