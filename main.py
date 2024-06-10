import json
import os
import random
import time

import tqdm

from get_tiku import get_tiku
from TKHandler import get_questionId
from get_questions import GetQuestionDetailForH5


with open("./paperid_all.json","r",encoding="utf-8") as f:
    for line in tqdm.tqdm(f.readlines()):
        json_line=json.loads(line)
        # planid就是tikuid
        paperid_ls=json_line["paperId_ls"]
        planid=json_line["planid"]
        # paperid是这张卷子的id
        for paperid in tqdm.tqdm(paperid_ls):
            os.makedirs(f"./save_dir/{planid}",exist_ok=True)


            file_name=f"./save_dir/{planid}/{paperid}.json"
            if os.path.exists(file_name):
                continue
            flag,questionId_ls=get_questionId(planid,paperid)
            # 遍历每一章

            with open(file_name,"w",encoding="utf-8") as f:
                f.write(json.dumps(
                    {
                        "paperid":paperid,
                        "questionId_ls":questionId_ls
                    }
                ,ensure_ascii=False))

            # time.sleep(random.randint(3,5))


        # dataid就是questionid
        # if not flag:
        #     continue
        # for questionId in tqdm.tqdm(questionId_ls,desc=paperid):
        #     flag,result=GetQuestionDetailForH5(tkid=planid,paperid=paperid,qid=questionId)
        #     #
        #     if not flag:
        #         continue
        #     result={
        #         "QuestionContent":result["QuestionContent"],
        #         "QuestionAnalysis":result["QuestionAnalysis"],
        #         "selectAnswer":result["selectAnswer"],
        #         "paperid":paperid,
        #         "planid":planid,
        #         "questionId":questionId
        #     }
        #     with open("./xiti.jsonl","a",encoding="utf-8") as f:
        #         f.write(json.dumps(result,ensure_ascii=False))
        #         f.write("\n")