# SmartEd - Making Learning Smarter

## Problem Statement

In the realm of higher education, students often grapple with the daunting task of efficiently collecting comprehensive notes and accessing high-quality study materials from their respective institutions. Recognizing the limitations of traditional learning resources, many turn to online platforms such as YouTube for lectures and tutorials. However, a prevalent challenge emerges when these educational videos are overly lengthy, hindering students' ability to concentrate and distill key information effectively.

## Solution

**SmartEd** stands as a groundbreaking solution, specifically designed to address the prevalent challenges faced by students in the modern `educational` landscape. This platform incorporates a suite of features meticulously crafted to enhance the `learning experience`.

## Features

### 1. Video Summarizer

SmartEd's Video Summarizer functionality begins by allowing users to input YouTube links. The platform then intricately interacts with the `YouTube server` to download `video transcripts`. Leveraging the `PALM API` model `(text-bison-001)`, SmartEd intelligently summarizes the content, offering users a concise and coherent overview of lengthy educational videos.

### 2. Text to Speech

Beyond traditional text-based summaries, SmartEd goes a step further by providing a Text to Speech feature. This functionality converts the summarized content into speech using the python module `pyttsx3`, catering to diverse learning preferences and enabling users to consume information through auditory means. This is particularly advantageous for users who prefer mobile learning or wish to review content while on the move.

### 3. Handwritten Notes to Text

SmartEd integrates advanced `Convolutional Neural Networks (CNN)` and `TensorFlow` algorithms to tackle the challenge of converting handwritten notes into digital text files. This transformative feature allows users to seamlessly transition their physical notes into a digital format, facilitating easier sharing, editing, and collaboration.

### 4. PDF Summarizer

Recognizing the ubiquity of PDF documents in academic settings, SmartEd offers a `PDF Summarizer`. To ensure efficient summarization without surpassing the PALM API's query limit (three queries per minute), the platform intelligently breaks down lengthy PDFs into manageable pages, summarizing each individually.

## Problems Faced

The development journey of SmartEd was not without its challenges. Integrating third-party APIs, especially managing rate limits, presented a significant hurdle. Additionally, ensuring the accuracy and coherence of the summarization process demanded meticulous fine-tuning of algorithms to meet the high standards set by the educational community.

## Architectural Diagram

<img src="preview/architecture.png" alt="Architectural Diagram"> 

## WebApp Preview

<img src="preview/image1.png" alt="Home page">
<img src="preview/image2.png" alt="Features page">
<img src="preview/image3.png" alt="Contact page">
<img src="preview/image4.png" alt="Register page">
<img src="preview/image5.png" alt="Dashboard Page">

## Future Scope

SmartEd envisions continuous growth and improvement. In the pipeline for future releases are:

### 1. Notes to Flow Chart

Expanding on the platform's capabilities, SmartEd plans to introduce a feature that converts textual notes into dynamic and interactive flow charts. This will be achieved through advanced `Natural language processing (NLP)` techniques, extracting crucial keywords and relationships.

### 2. Conversational Chat

SmartEd aims to implement a Conversational Chat feature, allowing users to engage in dialogue with the platform. This functionality will answer questions related to uploaded documents, provide additional context, and offer clarification on study materials.

## Setup and Contribution

1. **Clone the repository:**
   ```bash
   git clone https://github.com/deepraj21/SmartEd.git
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Google AI API Key:**
   Obtain your Google AI API key and configure it in the application:
   ```python
   palm.configure(api_key='YOUR_GOOGLE_API_KEY')
   ```

4. **Run the Application:**
   ```bash
   python app.py
   ```

   Visit `http://localhost:5000` in your web browser.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to the creators of the PALM API for their groundbreaking work.

## Conclusion

In conclusion, SmartEd represents a paradigm shift in educational technology. By making the learning process more efficient and accessible, SmartEd endeavors to empower students on their educational journey. The development team invites users to join in this educational revolution, providing valuable feedback to further refine and enhance SmartEd's capabilities. Together, we can make learning smarter, easier, and more enjoyable.



