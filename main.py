import json
import random
import time

import tqdm

from get_tiku import get_tiku
from TKHandler import get_questionId
from get_questions import GetQuestionDetailForH5


with open("./save_dir/record.json","r",encoding="utf-8") as f:
    for planid in f.readlines():
        # planid就是tikuid
        paperList=get_tiku(planid)
        paperid_ls=[e["paperID"] for each in paperList for e in each["paperList"]]
        paperid_ls=list(filter(lambda each: None if each=="" else each,paperid_ls))
        # paperid是这张卷子的id


        for paperid in tqdm.tqdm(paperid_ls):
            flag,questionId_ls=get_questionId(planid,paperid)
            # 遍历每一章

            with open("./paperid_questionId_ls.json","a",encoding="utf-8") as f:
                f.write(json.dumps(
                    {
                        "paperid":paperid,
                        "questionId_ls":questionId_ls
                    }
                ,ensure_ascii=False))
                f.write("\n")

            time.sleep(random.randint(3,5))


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