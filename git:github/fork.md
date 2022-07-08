## Fork

#### (GitHub) Fork

1. Fork할 저장소에서 우측 상단의 Fork 버튼 클릭

   ![image-20220707131112356](/Users/yuyeong/Desktop/TIL/git:github/fork.assets/image-20220707131112356.png)

2. 자신의 원격저장소에 저장될 이름을 작성 Create fork

   ![image-20220707131431617 (1)](/Users/yuyeong/Desktop/TIL/git:github/fork.assets/image-20220707131431617 (1).png)

3. 자신의 원격저장소에서 확인

   ![스크린샷 2022-07-08 오후 2.28.41](/Users/yuyeong/Desktop/TIL/git:github/fork.assets/스크린샷 2022-07-08 오후 2.28.41.png)

#### (Local) Clone & Branch 생성

1. Fork 받아온 저장소를 로컬로 clone 

   - ⭐️ clone URL 반드시 확인! 본인의 저장소여야 함

     ```bash
     $ git clone URL
     ```

     

     ![image-20220707132309235 (1)](/Users/yuyeong/Desktop/TIL/git:github/fork.assets/image-20220707132309235 (1).png)

2. branch를 생성하고 이동

   ```bash
   (master) $ git branch example
   (msater) $ git checkout example
   (example) $
   ```

   

   

#### (Local) 내용 폴더에 추가 하고 커밋!

- 작업 완료 후 변경 사항을 add, commit, push 

  ```bash
  (example) $ git add .
  (example) $ git commit -m "message"
  (example) $ git push origin example 
  ```

  

#### (GitHub) Pull Request

1. GirHub에서 compare & pull request 를 생성

   - 자동으로 초록 버튼이 생성되기도 하지만 안뜰때는 직접 pull request에 들어가서 만들어준다.

     ![image-20220707134616247](/Users/yuyeong/Desktop/TIL/git:github/fork.assets/image-20220707134616247.png)

2. pull request 내용을 작성한 후 create pull request

   - Head repository 와 base repository를 확인 !

   - Head → base 방향으로 merge 

     ![image-20220707141234516](/Users/yuyeong/Desktop/TIL/git:github/fork.assets/image-20220707141234516.png)