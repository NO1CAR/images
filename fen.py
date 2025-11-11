import os
import shutil
import math

def split_images_into_folders(source_folder, output_base="output"):
    """
    将源文件夹中的图片平均分配到4个子文件夹中
    :param source_folder: 包含图片的源文件夹路径
    :param output_base: 输出文件夹的基础名称
    """
    # 获取所有图片文件
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')
    images = [f for f in os.listdir(source_folder) 
              if os.path.isfile(os.path.join(source_folder, f)) 
              and f.lower().endswith(image_extensions)]
    
    if not images:
        print(f"在文件夹 {source_folder} 中没有找到图片文件")
        return
    
    total_images = len(images)
    print(f"找到 {total_images} 张图片")
    
    # 创建4个子文件夹
    folders = [os.path.join(output_base, f"folder_{i+1}") for i in range(4)]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
    
    # 计算每个文件夹应该包含的图片数量
    per_folder = math.ceil(total_images / 4)
    
    # 分配图片到各个文件夹
    for i, image in enumerate(images):
        src_path = os.path.join(source_folder, image)
        dest_folder = folders[i // per_folder]
        dest_path = os.path.join(dest_folder, image)
        
        try:
            shutil.copy2(src_path, dest_path)
            print(f"已复制: {image} -> {os.path.basename(dest_folder)}")
        except Exception as e:
            print(f"复制 {image} 失败: {str(e)}")
    
    print("\n图片分配完成:")
    for i, folder in enumerate(folders, 1):
        count = len(os.listdir(folder))
        print(f"文件夹 {i}: {count} 张图片")

if __name__ == "__main__":
    # 配置参数
    source_dir = r"C:\Users\qijing\Desktop\imgdownlod"  # 替换为你的图片文件夹路径
    output_dir = r"C:\Users\qijing\Desktop\imgdownlod"       # 替换为输出文件夹路径
    
    # 执行分配
    split_images_into_folders(source_dir, output_dir)