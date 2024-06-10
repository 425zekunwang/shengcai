import json
import os
import random
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

import tqdm

from get_tiku import get_tiku
from TKHandler import get_questionId
from get_questions import GetQuestionDetailForH5


def process_paper(planid, paperid):
    os.makedirs(f"./save_dir/{planid}", exist_ok=True)
    file_name = f"./save_dir/{planid}/{paperid}.json"
    if os.path.exists(file_name):
        return

    flag, questionId_ls = get_questionId(planid, paperid)
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(json.dumps({"paperid": paperid, "questionId_ls": questionId_ls}, ensure_ascii=False))
    # Simulate delay
    time.sleep(random.randint(3, 5))


def main():
    with open("./paperid_all.json", "r", encoding="utf-8") as f:
        lines = f.readlines()

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = []

        for line in tqdm.tqdm(lines):
            json_line = json.loads(line)
            paperid_ls = json_line["paperId_ls"]
            planid = json_line["planid"]

            for paperid in paperid_ls:
                futures.append(executor.submit(process_paper, planid, paperid))

        for future in tqdm.tqdm(as_completed(futures), total=len(futures)):
            future.result()

    # The following code is commented out but can be used for further processing
    # for line in tqdm.tqdm(lines):
    #     json_line = json.loads(line)
    #     paperid_ls = json_line["paperId_ls"]
    #     planid = json_line["planid"]

    #     for paperid in paperid_ls:
    #         file_name = f"./save_dir/{planid}/{paperid}.json"
    #         if not os.path.exists(file_name):
    #             continue

    #         with open(file_name, "r", encoding="utf-8") as f:
    #             data = json.load(f)
    #             questionId_ls = data["questionId_ls"]

    #         for questionId in tqdm.tqdm(questionId_ls, desc=paperid):
    #             flag, result = GetQuestionDetailForH5(tkid=planid, paperid=paperid, qid=questionId)
    #             if not flag:
    #                 continue
    #             result = {
    #                 "QuestionContent": result["QuestionContent"],
    #                 "QuestionAnalysis": result["QuestionAnalysis"],
    #                 "selectAnswer": result["selectAnswer"],
    #                 "paperid": paperid,
    #                 "planid": planid,
    #                 "questionId": questionId
    #             }
    #             with open("./xiti.jsonl", "a", encoding="utf-8") as f:
    #                 f.write(json.dumps(result, ensure_ascii=False))
    #                 f.write("\n")


if __name__ == "__main__":
    main()
