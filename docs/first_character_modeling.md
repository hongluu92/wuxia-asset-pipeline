# Bước 2 — Dựng nhân vật Võ Đang đầu tiên

Character ID: `wudang_male_01`

## Concept chuẩn
- 4 views: front, back, right profile, 3/4.
- Tóc đen buộc cao, áo ngoài xanh navy, lớp áo trong trắng.
- Đai lưng đen với ngọc xanh, bảo vệ cẳng tay, giày tối, kiếm thẳng jian.
- Reference: `ArtPipeline/concepts/wudang_male_01/wudang_sheet_main.png` (đường dẫn mục tiêu; kiểm tra tên file thực tế trong repo).

## Free base đã chọn
- Tên: Quaternius Universal Base Characters
- Source: https://quaternius.itch.io/universal-base-characters
- License: CC0 1.0 (theo trang pack, cần giữ snapshot theo file tải)
- Download: Standard ZIP, khoảng 122 MB, mẫu **Regular Male**.
- Formats: FBX, glTF.
- Base có Humanoid rig, chưa có bộ animation cần thiết.

## Mac M4 16 GB — quy trình Blender
1. Tải bản Standard, giải nén ở `ArtPipeline/free_assets/quaternius_universal_base_characters/` trên máy cá nhân.
2. Chọn model nam Regular và import FBX/glTF vào Blender 4.5 LTS.
3. Lưu ngay file `ArtPipeline/blender/wudang_male_01.blend`.
4. Xác nhận body và armature tồn tại, model giữ nguyên rig trước khi chỉnh áo.
5. Lập blockout trang phục: navy outer robe, white inner layer, belt, forearm guards, boots, ponytail, straight sword.
6. Kiểm tra hình dáng ở camera góc 3/4 và từ phía sau.
7. Chưa rig thêm cloth physics; giữ tà áo ngắn/gọn để tránh xuyên khi chạy.
8. Giữ sword mesh riêng, đặt vị trí ở tay phải hoặc socket sau khi kiểm thử rig.

## Tiêu chí nghiệm thu
- [ ] Base model có license và link nguồn.
- [ ] Blender scene mở được trên Mac M4.
- [ ] Có armature và nhân vật có thể đổi pose.
- [ ] Silhouette võ hiệp nhận ra ở camera 3/4.
- [ ] Giữ các dấu hiệu: xanh-trắng, tóc buộc cao, đai ngọc, jian.
- [ ] Các mesh trang bị được đặt tên và tách rời.

## Sau bước này
Tạo 3 clip Idle, Walk, Attack bằng Mixamo hoặc thư viện animation có rig tương thích. Sau đó test một hướng rồi mới render đủ 8 hướng.
