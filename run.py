from apscheduler.schedulers.blocking import BlockingScheduler
from crawling.cgv_crawling import imax_movie
from slack.message import slack_message

if __name__ == '__main__':
    sched = BlockingScheduler()
    sched.add_job(slack_message(imax_movie), 'cron', hour='9')  # 매일 아홉시 기준으로 메시지 스케줄링
    sched.start()