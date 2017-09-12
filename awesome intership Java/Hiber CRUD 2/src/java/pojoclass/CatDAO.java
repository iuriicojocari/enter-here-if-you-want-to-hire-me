/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pojoclass;

import java.sql.SQLException;
import java.util.Collection;

/**
 *
 * @author YURIES
 */
public interface CatDAO {

    public void addCat(CatPOJO cat) throws SQLException;

    public void updateCat(Long cat_id, CatPOJO cat) throws SQLException;

    public CatPOJO getCatById(Long id) throws SQLException;

    public Collection getAllCats() throws SQLException;

    public void deleteCat(CatPOJO bus) throws SQLException;

    public void DeleteCatById(Long cat_id) throws SQLException;
}
