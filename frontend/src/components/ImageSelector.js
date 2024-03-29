import React, { useState } from 'react';

const ImageSelector = ({ imageUrl, updateImage}) => {
  const [selectedImage, setSelectedImage] = useState(imageUrl);

  const handleImageChange = (event) => {
    const file = event.target.files[0];
    const imageSrc = URL.createObjectURL(file);
    setSelectedImage(imageSrc);
    updateImage(file);
  };

  return (
    <div className="flex flex-col items-center justify-center p-4">
      {selectedImage && (
        <img
          src={selectedImage}
          alt="Selected"
          className="w-48 h-48 object-cover rounded-lg shadow-lg w-32 h-32 rounded-full object-cover"
        />
      )}
    <div className='flex justify-center items-center w-full mt-4'>
        <input type="file" className="text-sm text-gray-500
            file:mr-4 file:py-2 file:px-4
            file:rounded-full file:border-0
            file:text-sm file:font-semibold
            file:bg-violet-50 file:text-violet-700
            hover:file:bg-violet-100 mt-4"
            onChange={handleImageChange}
        />
    </div>
    </div>
  );
};

export default ImageSelector;
