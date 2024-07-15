# 패키지 및 모듈은 샘플 코드 관련 페이지라 생략


class Auto_Home():
    """
        Auto_Home Class 사용
        지마켓 홈섹션
        기존에 작성한 코드 포폴 예시로 작성
    """


    # 지마켓 앱 스크롤 코드
    def __scroll_mobile_app(self, location, xpath, scroll_amount, max_scroll_count):
        """

        요소가 화면에 보일때까지 스크롤
        :param (str) location : 스크롤하려는 방향 / 1: 아래에서 위로 스와이프 / 2: 위에서 아래로 스와이프
        :param (str) xpath: 찾으려는 요소
        :param (int) scroll_amount: 한번 스크롤시 이동하는 정도(1~10 사이에서 결정하며 숫자가 클수록 많이 이동)
        :param (int) max_scroll_count: 최대 스크롤 횟수 (스크롤 횟수에 도달할때까지 요소를 찾지 못하면 raise 발생)
        :return: 없음
        :example: __scroll_mobile_app(self,"1",xpath,3,20) # 해당 요소를 찾을 때까지 아래에서 위로 최대 20번 스크롤 진행

        """
        scroll_count = 0
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']

        k = (height / 20) * scroll_amount

        while True:
            try:
                time.sleep(5)
                self.driver.implicitly_wait(5)
                element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
                if element.location['y'] > (height * 2 / 3):
                    loc = element.location
                    new_y = loc['y']
                    self.driver.swipe(width / 2, height / 2, width / 2, (height / 2) - k / 2)
                    if element.location['y'] == new_y:
                        print("스와이프 끝부분 도달")
                        break
                    print("위치 조정")
                elif element.location['y'] < (height * 1 / 3):
                    loc = element.location
                    new_y = loc['y']
                    self.driver.swipe(width / 2, height / 2, width / 2, (height / 2) + k / 2)
                    if element.location['y'] == new_y:
                        print("스와이프 끝부분 도달")
                        break
                    print("위치 조정")
                else:
                    print("요소 발견됨")
                    break
            except:
                scroll_count += 1
                if scroll_count > max_scroll_count:
                    print("최대 스크롤 횟수 초과")
                    raise Exception("요소를 찾을 수 없음")

                print("스크롤 진행 중 ({}회)".format(scroll_count))
                if location == "1":
                    self.driver.swipe(width / 2, height / 2, width / 2, (height / 2) - k)
                elif location == "2":
                    self.driver.swipe(width / 2, height / 2, width / 2, (height / 2) + k)
                else:
                    print("#", "스와이프할 방향을 지정해주세요.")
                    raise

            finally:
                # try 블록 이후에 원래의 implicit_wait 값으로 복원
                self.driver.implicitly_wait(self.implicit_wait)



        # 지마켓 한 섹션 uiux 자동화 샘플 코드

    def ss_1_2_2_9(self, use_type, *args):
        """

        1.2.2-9)홈쇼핑 > 홈쇼핑 별 BEST

            :param (int) use_type: 사용 여부 (1: 미사용 / 2: 사용)
            :param (str) args[0] : 홈쇼핑 별 BEST 문구
            :param (str) args[1] : 아이템 카드 노출 갯수
            :param (str) args[2] : 전체보기 버튼 문구
            :return: 없음
            :example: gmarket_regression_home_gnb_page_param.ss_1_2_2_9(['홈쇼핑 별 BEST', 4, '전체보기'])

        """

        if use_type == 2:

            HomeGnbPageParam.__select_home_section(self, "홈쇼핑")

            # 홈쇼핑 > 홈쇼핑 별 BEST 영역 노출 확인
            runtext = '홈쇼핑 > 홈쇼핑 별 BEST 영역 노출 확인'
            print("#", runtext, "시작")
            xpath = '//android.view.ViewGroup[@content-desc="홈쇼핑 별 BEST"]'
            HomeGnbPageParam.__scroll_mobile_app(self, "1", xpath, 8, 10)
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            value1 = element.get_attribute('content-desc')  # '홈쇼핑 별 BEST'
            assert_that(value1).is_in(args[0])
            print("#", runtext, "종료")

            # 홈쇼핑 > 홈쇼핑 별 BEST > 홈쇼핑 브랜드 영역 좌우 스와이핑 동작 확인
            runtext = '홈쇼핑 > 홈쇼핑 별 BEST > 홈쇼핑 브랜드 영역 좌우 스와이핑 동작 확인'
            print("#", runtext, "시작")
            xpath = '(//android.widget.RelativeLayout[@resource-id="com.ebay.kr.gmarket:id/rlBackGround"])[3]'
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            start_x = element.location['x']
            start_y = element.location['y']
            end_x = start_x - 200
            end_y = start_y
            self.driver.swipe(start_x, start_y, end_x, end_y)
            print("#", runtext, "종료")

            value2 = list()
            for i in range(len(args[1])):
                # 홈쇼핑 > 카테고리 8개 노출 확인
                runtext = '홈쇼핑 > 카테고리 8개 노출 확인'
                print("#", runtext, "시작")
                xpath = '//android.widget.RadioButton[@resource-id="com.ebay.kr.gmarket:id/tvName" and @text="{0}"]'.format(
                    args[1][i])
                element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
                start_x = element.location['x']
                start_y = element.location['y']
                end_x = start_x - 200
                end_y = start_y
                self.driver.swipe(start_x, start_y, end_x, end_y)
                value2.append(element.text)
                print("#", runtext, "종료")
                time.sleep(5)

            assert_that(value2).is_in(args[1])

            # 홈쇼핑 > 홈쇼핑 별 BEST > 아이템카드 2X2/ 4개 노출 확인
            runtext = '홈쇼핑 > 홈쇼핑 별 BEST > 아이템카드 2X2/ 4개 노출 확인'
            print("#", runtext, "시작")
            xpath = '//android.widget.TextView[@resource-id="com.ebay.kr.gmarket:id/tvIndex" and @text="4"]'
            HomeGnbPageParam.__scroll_mobile_app(self, "1", xpath, 5, 5)
            value3 = 0
            for i in range(4):
                k = i + 1
                xpath = '(//androidx.recyclerview.widget.RecyclerView[@resource-id="com.ebay.kr.gmarket:id/rvList"])[1]/android.view.ViewGroup[{0}]'.format(
                    k)
                try:
                    element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
                    print("#", k, "요소 찾음")
                    value3 = value3 + 1
                except:
                    print("#", "요소 못찾음")
                    element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
                    break
            time.sleep(5)
            assert_that(value3).is_in(args[2])
            print("#", runtext, "종료")

            # 홈쇼핑 > 홈쇼핑 별 BEST > 영역 하단에 홈쇼핑 브랜드+전체보기 버튼 노출 확인
            runtext = '홈쇼핑 > 홈쇼핑 별 BEST > 영역 하단에 홈쇼핑 브랜드+전체보기 버튼 노출 확인'
            print("#", runtext, "시작")
            xpath = '//android.widget.TextView[@resource-id="com.ebay.kr.gmarket:id/tvTitleSub"]'
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            value4 = element.text  # '전체보기'
            assert_that(value4).is_in(args[3])
            print("#", runtext, "종료")



        else:
            print("#", "Home_section 1_2_2_9 Test Case 실행 생략")