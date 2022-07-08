## Fork

#### (GitHub) Fork

1. Fork할 저장소에서 우측 상단의 Fork 버튼 클릭

![image-20220707131112356](https://user-images.githubusercontent.com/108647801/177930108-6d32312f-d71c-41d7-9b14-2d05b40adbcc.png)

2. 자신의 원격저장소에 저장될 이름을 작성 Create fork

![image-20220707131431617 (1)](https://user-images.githubusercontent.com/108647801/177930113-c75b2999-199b-4ca1-b0e2-b925a0a95f2e.png)


3. 자신의 원격저장소에서 확인

 <img width="384" alt="스크린샷 2022-07-08 오후 2 28 41" src="https://user-images.githubusercontent.com/108647801/177930126-b27a7730-120d-4670-8a0f-cb48b9a5591e.png">

#### (Local) Clone & Branch 생성

1. Fork 받아온 저장소를 로컬로 clone 

   - ⭐️ clone URL 반드시 확인! 본인의 저장소여야 함

     ```bash
     $ git clone URL
     ```

     

![image-20220707132309235 (1)](https://user-images.githubusercontent.com/108647801/177930155-b3391ef7-eb86-45a0-bbfd-14457c09a4e8.png)

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

   ![image-20220707134616247](https://user-images.githubusercontent.com/108647801/177930187-82bf1aec-e92b-4d4f-ba02-6b55028aa31b.png)

2. pull request 내용을 작성한 후 create pull request

   - Head repository 와 base repository를 확인 !

   - Head → base 방향으로 merge 

  ![image-20220707141234516](https://user-images.githubusercontent.com/108647801/177930203-4b3cb23a-506a-4e3c-9e92-a81a356a07a6.png)
