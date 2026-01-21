import { useState, useCallback } from 'react';

// Window state management hook
// Following BMAD-METHOD: Simple, Testable, Antifragile
export const useWindowManager = () => {
  const [windows, setWindows] = useState([]);

  const openWindow = useCallback((osId, osDefinition) => {
    const newWindow = {
      id: `${osId}-${Date.now()}`,
      osId,
      osDefinition,
      position: { x: 100 + windows.length * 30, y: 100 + windows.length * 30 },
      size: { width: 800, height: 600 },
      isMinimized: false,
      zIndex: windows.length,
    };
    setWindows((prev) => [...prev, newWindow]);
  }, [windows.length]);

  const closeWindow = useCallback((windowId) => {
    setWindows((prev) => prev.filter((w) => w.id !== windowId));
  }, []);

  const minimizeWindow = useCallback((windowId) => {
    setWindows((prev) =>
      prev.map((w) =>
        w.id === windowId ? { ...w, isMinimized: !w.isMinimized } : w
      )
    );
  }, []);

  const focusWindow = useCallback((windowId) => {
    setWindows((prev) => {
      const maxZ = Math.max(...prev.map((w) => w.zIndex), 0);
      return prev.map((w) =>
        w.id === windowId ? { ...w, zIndex: maxZ + 1 } : w
      );
    });
  }, []);

  const updateWindowPosition = useCallback((windowId, position) => {
    setWindows((prev) =>
      prev.map((w) => (w.id === windowId ? { ...w, position } : w))
    );
  }, []);

  const updateWindowSize = useCallback((windowId, size) => {
    setWindows((prev) =>
      prev.map((w) => (w.id === windowId ? { ...w, size } : w))
    );
  }, []);

  return {
    windows,
    openWindow,
    closeWindow,
    minimizeWindow,
    focusWindow,
    updateWindowPosition,
    updateWindowSize,
  };
};
