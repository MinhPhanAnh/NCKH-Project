from pydantic import BaseModel
from utils import clean_text
from openai import OpenAI
import os
import json

# Access the OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API key không được cung cấp!")

client = OpenAI(api_key=api_key)

class QuizSample(BaseModel):
    question: str
    choices: list[str]
    answer: str

class Exam(BaseModel):
    quizes: list[QuizSample]

class BaseExtracter():
    def __init__(self):
        self.model_name = "gpt-4o"

    def run(self, text, num_questions):
        pass

    @staticmethod
    def ensure_unique_questions(questions):
        """Loại bỏ các câu hỏi trùng lặp dựa trên nội dung câu hỏi."""
        seen = set()
        unique_questions = []
        for q in questions:
            if q["question"] not in seen:
                seen.add(q["question"])
                unique_questions.append(q)
        return unique_questions

class ExtractA(BaseExtracter):
    def run(self, _input, num_questions):
        completion = client.beta.chat.completions.parse(
            model=self.model_name,
            messages=[
                {
                    "role": "system",
                    "content": f"""
                        TASK: Extract {num_questions} questions of level A difficulty. 
                        Each question should be simple and straightforward, testing basic knowledge or comprehension skills.
                        Provide the output in the format of a list of dictionaries: 
                        question (text), choices (list of 4 options: A, B, C, D), and answer (correct answer).
                        RULE: Use Vietnamese for all questions, choices, and answers.
                        """
                },
                {
                    "role": "user",
                    "content": f"base on this document: {clean_text(_input)}"
                },
            ],
            response_format=Exam,
        )
        res = json.loads(completion.choices[0].message.content)
        res["quizes"] = self.ensure_unique_questions(res["quizes"])
        for i in range(len(res["quizes"])):
            res["quizes"][i]["level"] = "Nhận biết"
        return res

class ExtractB(ExtractA):
    def run(self, _input, num_questions):
        completion = client.beta.chat.completions.parse(
            model=self.model_name,
            messages=[
                {
                    "role": "system",
                    "content": f"""
                        TASK: Extract {num_questions} questions of level B difficulty. 
                        Each question should test understanding and the ability to explain or interpret information.
                        Provide the output in the format of a list of dictionaries: 
                        question (text), choices (list of 4 options: A, B, C, D), and answer (correct answer).
                        RULE: Use Vietnamese for all questions, choices, and answers.
                        """
                },
                {
                    "role": "user",
                    "content": f"base on this document: {clean_text(_input)}"
                },
            ],
            response_format=Exam,
        )
        res = json.loads(completion.choices[0].message.content)
        res["quizes"] = self.ensure_unique_questions(res["quizes"])
        for i in range(len(res["quizes"])):
            res["quizes"][i]["level"] = "Thông hiểu"
        return res

class ExtractC(ExtractA):
    def run(self, _input, num_questions):
        completion = client.beta.chat.completions.parse(
            model=self.model_name,
            messages=[
                {
                    "role": "system",
                    "content": f"""
                        TASK: Extract {num_questions} questions of level C difficulty. 
                        Each question should test the ability to apply knowledge to solve problems or perform tasks.
                        Provide the output in the format of a list of dictionaries: 
                        question (text), choices (list of 4 options: A, B, C, D), and answer (correct answer).
                        RULE: Use Vietnamese for all questions, choices, and answers.
                        """
                },
                {
                    "role": "user",
                    "content": f"base on this document: {clean_text(_input)}"
                },
            ],
            response_format=Exam,
        )
        res = json.loads(completion.choices[0].message.content)
        res["quizes"] = self.ensure_unique_questions(res["quizes"])
        for i in range(len(res["quizes"])):
            res["quizes"][i]["level"] = "Vận dụng"
        return res

class ExtractD(ExtractA):
    def run(self, _input, num_questions):
        completion = client.beta.chat.completions.parse(
            model=self.model_name,
            messages=[
                {
                    "role": "system",
                    "content": f"""
                        TASK: Extract {num_questions} questions of level D difficulty. 
                        Each question should test the ability to analyze, evaluate, or create based on complex or abstract information.
                        Provide the output in the format of a list of dictionaries: 
                        question (text), choices (list of 4 options: A, B, C, D), and answer (correct answer).
                        RULE: Use Vietnamese for all questions, choices, and answers.
                        """
                },
                {
                    "role": "user",
                    "content": f"base on this document: {clean_text(_input)}"
                },
            ],
            response_format=Exam,
        )
        res = json.loads(completion.choices[0].message.content)
        res["quizes"] = self.ensure_unique_questions(res["quizes"])
        for i in range(len(res["quizes"])):
            res["quizes"][i]["level"] = "Vận dụng cao"
        return res
