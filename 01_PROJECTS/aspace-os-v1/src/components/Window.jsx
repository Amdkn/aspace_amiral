import React, { useRef, useEffect, useState } from 'react';
import { Dashboard } from './Dashboard';

// Window Component - Draggable, Resizable, Modular
// BMAD: Independent, Self-contained, Testable
export const Window = ({
  window: windowState,
  onClose,
  onMinimize,
  onFocus,
  onUpdatePosition,
}) => {
  const windowRef = useRef(null);
  const headerRef = useRef(null);
  const [isDragging, setIsDragging] = useState(false);
  const [dragOffset, setDragOffset] = useState({ x: 0, y: 0 });

  // Drag handling
  useEffect(() => {
    if (!isDragging) return;

    const handleMouseMove = (e) => {
      const newX = e.clientX - dragOffset.x;
      const newY = e.clientY - dragOffset.y;
      onUpdatePosition(windowState.id, {
        x: Math.max(0, Math.min(newX, globalThis.innerWidth - 200)),
        y: Math.max(0, Math.min(newY, globalThis.innerHeight - 200)),
      });
    };

    const handleMouseUp = () => {
      setIsDragging(false);
    };

    document.addEventListener('mousemove', handleMouseMove);
    document.addEventListener('mouseup', handleMouseUp);

    return () => {
      document.removeEventListener('mousemove', handleMouseMove);
      document.removeEventListener('mouseup', handleMouseUp);
    };
  }, [isDragging, dragOffset, windowState.id, onUpdatePosition]);

  const handleMouseDown = (e) => {
    if (e.target === headerRef.current || headerRef.current.contains(e.target)) {
      setIsDragging(true);
      setDragOffset({
        x: e.clientX - windowState.position.x,
        y: e.clientY - windowState.position.y,
      });
      onFocus(windowState.id);
    }
  };

  const colorClasses = {
    solar: 'from-solar-500 to-solar-600',
    nature: 'from-nature-500 to-nature-600',
    sky: 'from-sky-500 to-sky-600',
  };

  const gradientClass = colorClasses[windowState.osDefinition.color] || colorClasses.sky;

  if (windowState.isMinimized) {
    return null;
  }

  return (
    <div
      ref={windowRef}
      className="fixed glass rounded-xl overflow-hidden shadow-2xl"
      style={{
        left: `${windowState.position.x}px`,
        top: `${windowState.position.y}px`,
        width: `${windowState.size.width}px`,
        height: `${windowState.size.height}px`,
        zIndex: windowState.zIndex,
      }}
      onMouseDown={() => onFocus(windowState.id)}
    >
      {/* Window Header */}
      <div
        ref={headerRef}
        className={`
          drag-handle
          bg-gradient-to-r ${gradientClass}
          px-4 py-3
          flex items-center justify-between
          cursor-move
        `}
        onMouseDown={handleMouseDown}
      >
        <div className="flex items-center gap-2">
          <span className="text-2xl">{windowState.osDefinition.icon}</span>
          <h3 className="text-white font-semibold">
            {windowState.osDefinition.name}
          </h3>
        </div>
        
        <div className="flex items-center gap-2">
          {/* Minimize Button */}
          <button
            onClick={(e) => {
              e.stopPropagation();
              onMinimize(windowState.id);
            }}
            className="w-6 h-6 rounded-full bg-yellow-400 hover:bg-yellow-500 transition-colors flex items-center justify-center text-xs font-bold text-white"
            title="Minimize"
          >
            −
          </button>
          
          {/* Close Button */}
          <button
            onClick={(e) => {
              e.stopPropagation();
              onClose(windowState.id);
            }}
            className="w-6 h-6 rounded-full bg-red-400 hover:bg-red-500 transition-colors flex items-center justify-center text-xs font-bold text-white"
            title="Close"
          >
            ×
          </button>
        </div>
      </div>

      {/* Window Content */}
      <div className="bg-white/90 h-[calc(100%-48px)] overflow-hidden">
        {windowState.osDefinition.type === 'internal' ? (
          <Dashboard osId={windowState.osId} />
        ) : (
          <iframe
            src={windowState.osDefinition.defaultUrl}
            className="w-full h-full border-0"
            title={windowState.osDefinition.name}
            sandbox="allow-same-origin allow-scripts allow-forms"
          />
        )}
      </div>
    </div>
  );
};
