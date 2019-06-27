import uiautomator2 as u2
from time import sleep

connect_ = u2.connect("HBSBB19302501165")
print(connect_)
connect_.reset_uiautomator()
# connect_.healthcheck()

connect_.debug = True
connect_.implicitly_wait(10.0)
# connect_.info

# connect_.wait_activity(timeout=10.0)

# connect_.app_start("com.syrs.pwcn")
with connect_.session("com.syrs.pwcn") as sess:
    # sess.watchers.watched = True

    # 判断是否是活动界面
    jump = sess(text="跳过")
    if jump.exists:
        jump.click()
    # 获取页面内容
    x = sess(resourceId = "com.syrs.pwcn:id/rl_login_pwd")
    if x.exists:
        x.click()
        sess(resourceId = "com.syrs.pwcn:id/et_phonenum").send_keys(13301314544)
        sess(resourceId = "com.syrs.pwcn:id/et_login_pwd").send_keys("123456a")
        sess(resourceId = "com.syrs.pwcn:id/btn_login").click()
    sess(text="善源公益").wait(True)
    # 进入到善源公益界面
    gongyi_ = sess(text="善源公益", className="android.view.View", instance=1)
    if gongyi_:
        gongyi_.click()
        connect_.xpath("//android.view.View[@text='善源公益']").wait(10)
        # sess(beta="//android.view.View[@text='善源公益']").wait(True,3.0)
        sess(text="教育助学").wait(True,30)
        sess(text="教育助学").click()
        sess(text=u"目标金额/元").click()

        # 单笔捐
        donation = sess(text="单笔捐")
        donation.click()
        sess.watcher("WATCHER_NAME").when(text="捐赠信息")
        sess.watchers.run()
        sess(text="1").click()
        # sess.press("back")
        sess(text="支付宝").click()
        sess(text="确认支付").click()
        sess.watchers.remove("WATCHER_NAME")
        sleep(2)
        # sess.press("back")
        if sess(resourceId="com.android.systemui:id/back").click_exists():
            print("====yes")
            sleep(2)
            sess.press("back")

        # sess.press("back")
        # mm = connect_(resourceId="com.android.systemui:id/back", description="返回")
        # connect_(resourceId="com.android.systemui:id/back", description="返回").click()
        # with connect_.session("com.eg.android.AlipayGphone") as aliPaySes:
        #     aliPaySes(className="android.widget.ImageView", instance=16).click()
        # connect_.press("back")

        connect_(text="确定").click()
        sess.press("back")
        sess.press("back")
        sess.press("back")


    if sess(resourceId = "com.syrs.pwcn:id/id_iv5").wait(True, timeout=3):
        sess(resourceId="com.syrs.pwcn:id/id_iv5").click()
        sess(text="钱包余额").wait(True,timeout=4)
        if sess(text="钱包余额").exists:
            print("用户已经登录成功......")
        else:
            print("登录界面个人中心登录出现异常......")
    # 操作进行退出动作
    login_tag = sess(scrollable=True).scroll.toEnd()
    setter = sess(text="设置")
    setter.wait(True,timeout=2)
    setter.click()
    login_out = sess(text="退出登录")
    login_out.wait(True)
    login_out.click()
    connect_(resourceId="android:id/button1").click()

    sleep(9)
    # sess.close()

# sleep(5)
# connect_.app_stop("com.syrs.pwcn")
# sleep(2)
# connect_.app_start("com.syrs.pwcn")